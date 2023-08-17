from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('search_results/', views.search_results, name='search_results'),
    # 다른 URL 패턴들 추가
]
