from django.shortcuts import render
from django.db import connection

# Create your views here.
def main(request):
    return render(request, "base.html")