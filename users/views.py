from django.shortcuts import render
from .models import UserModel

# Create your views here.
def log_in(request):
    return render(request, 'login.html')

def sign_up (request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password != password2:
            return render(request, 'signup.html', {'error':'패스워드를 확인해 주세요'})
        else:
            exist_guest = UserModel.objects.filter(username=username)
            if exist_guest:
                return render(request, 'signup.html', {'error':'이미 존재하는 유저입니다'})
            else:
                new_guest = UserModel()
                new_guest.username = username
                new_guest.name = name
                new_guest.password = password
                new_guest.save()
                return render(request, 'login.html')