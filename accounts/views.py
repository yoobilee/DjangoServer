from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

# Create your views here.
def agency_signup(request):
    return render(request, 'agency_signup.html')

def influencer_signup(request):
    return render(request, 'influencer_signup.html')