from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from .models import Keyword

# Create your views here.
def Influencer1(request):
    first_keyword = Keyword.objects.filter(username='b.saem').order_by('weights').first()
    return render(request, 'Influencer1.html', {'first_keyword': first_keyword})

def Influencer2(request):
    Keyword = Keyword.objects.all()  
    return render(request, 'Influencer2.html',{'keyword': Keyword})

def keyword_list(request):
    keyword_list = Keyword.objects.all()
    return render(request, 'keyword_list.html', {'keyword_list': keyword_list})