from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from django.contrib.auth import logout
from .models import YourModel

# Create your views here.
def first_index(request):
    logout(request)
    return render(request, "first-index.html")

def InfluHome(request):
    return render(request, "InfluHome.html")

def AdvHome(request):
    return render(request, "AdvHome.html")

def inner_page(request):
    return render(request, "inner-page.html")

def portfolio_details(request, pk):
    item = get_object_or_404(YourModel, pk=pk)
    
    # query = request.GET.get('q')
    # if query and query in item.body:
    #     return redirect('search-results', q=query)
    
    context = {'item': item}
    return render(request, 'portfolio-details.html', context)

def portfolio_details01(request):
    return render(request, "portfolio-details01.html")

def TermOfUse_A(request):
    return render(request, "TermOfUse_A.html")

def PrivacyPolicy_A(request):
    return render(request, "PrivacyPolicy_A.html")

def TermOfUse_I(request):
    return render(request, "TermOfUse_I.html")

def PrivacyPolicy_I(request):
    return render(request, "PrivacyPolicy_I.html")
