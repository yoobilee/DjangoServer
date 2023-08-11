from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Item

# Create your views here.
def search(request):
    query = request.GET.get('q')

    if query:
        results = Item.objects.filter(name__icontains=query)
    else:
        results = []

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'search.html', context)