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

def Influencer3(request):
    Keyword = Keyword.objects.all()  
    return render(request, 'Influencer3.html',{'keyword': Keyword})

def Influencer4(request):
    Keyword = Keyword.objects.all()  
    return render(request, 'Influencer4.html',{'keyword': Keyword})

def Influencer5(request):
    Keyword = Keyword.objects.all()  
    return render(request, 'Influencer5.html',{'keyword': Keyword})

def Influencer6(request):
    Keyword = Keyword.objects.all()  
    return render(request, 'Influencer6.html',{'keyword': Keyword})

def Influencer7(request):
    Keyword = Keyword.objects.all()  
    return render(request, 'Influencer7.html',{'keyword': Keyword})

def Influencer8(request):
    Keyword = Keyword.objects.all()  
    return render(request, 'Influencer8.html',{'keyword': Keyword})

def Influencer9(request):
    Keyword = Keyword.objects.all()  
    return render(request, 'Influencer9.html',{'keyword': Keyword})