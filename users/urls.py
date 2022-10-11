from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up, name='sing_up'), #회원가입
    path('log-in/', views.log_in, name='log_in') #로그인화면
]