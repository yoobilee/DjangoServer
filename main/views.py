from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection

# Create your views here.
def first_index(request):
    return render(request, "first-index.html")

def InfluHome(request):
    return render(request, "InfluHome.html")

def AdvHome(request):
    return render(request, "AdvHome.html")

def inner_page(request):
    return render(request, "inner-page.html")

def portfolio_details(request):
    return render(request, "portfolio-details.html")