from django.shortcuts import render
from django.db import connection

# Create your views here.
def base(request):
    return render(request, "base.html")

def inner_page(request):
    return render(request, "inner-page.html")

def portfolio_details(request):
    return render(request, "portfolio-details.html")