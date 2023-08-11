from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

# Create your views here.
def Influencer1(request):
    return render(request, 'Influencer1.html')