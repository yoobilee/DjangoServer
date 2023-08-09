from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

# Create your views here.
def Adv_Login(request):
    return render(request, 'Adv_Login.html')

def Adv_Signup(request):
    return render(request, 'Adv_Signup.html')

def Influ_Login(request):
    return render(request, 'Influ_Login.html')

def Influ_Signup(request):
    return render(request, 'Influ_Signup.html')

def Adv_Logout(request):
    return render(request, 'AdvHome.html')

def Influ_Logout(request):
    return render(request, 'InfluHome.html')

def MyPage(request):
    return render(request, 'MyPage.html')