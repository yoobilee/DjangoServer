from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .models import Influencer, Post_limmiae, Post_10_12_16yp, Post_b_saem, Post_wescsp1121, Post_vevi_d_live, Post_yakstory119

# Create your views here.
def Adv_Login(request):
    return render(request, 'Adv_Login.html')

def Influ_Login(request):
    return render(request, 'Influ_Login.html')

# your_app/views.py

def Adv_SignUp(request):
    influencers = Influencer.objects.all()
    return render(request, 'Adv_SignUp.html', {'influencers': influencers})

def Influ_SignUp(request):
    influencers = Influencer.objects.all()
    return render(request, 'Influ_SignUp.html', {'influencers': influencers})