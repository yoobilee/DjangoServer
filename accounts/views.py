from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

# Create your views here.
def Adv_Login(request):
    return render(request, 'Adv_Login.html')

def Influ_Login(request):
    return render(request, 'Influ_Login.html')