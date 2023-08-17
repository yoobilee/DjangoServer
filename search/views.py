from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

from main.models import YourModel

def search_results(request):
    query = request.GET.get('q')
    if query:
        items = YourModel.objects.filter(body__contains=query)  # body 필드에 검색어가 포함된 아이템들을 필터링합니다.
    else:
        items = YourModel.objects.none()

    context = {'query': query, 'items': items}
    return render(request, 'search_results.html', context)
