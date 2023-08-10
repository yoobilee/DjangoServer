from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .models import Influencer, Post_limmiae, Post_10_12_16yp, Post_b_saem, Post_wescsp1121, Post_vevi_d_live, Post_yakstory119, Post_iam_yaksa, Post_yakstagram, Post_pt_jjuny, User_adv, User_influ

# Create your views here.
def Adv_Login(request):
    return render(request, 'Adv_Login.html')

def Adv_Signup(request):
    influencers = Influencer.objects.all()
    return render(request, 'Adv_Signup.html', {'influencers': influencers})

def Influ_Login(request):
    return render(request, 'Influ_Login.html')

def Influ_Signup(request):
    influencers = Influencer.objects.all()
    return render(request, 'Influ_Signup.html', {'influencers': influencers})

def Adv_Logout(request):
    return render(request, 'AdvHome.html')

def Influ_Logout(request):
    return render(request, 'InfluHome.html')

def MyPage(request):
    return render(request, 'MyPage.html')