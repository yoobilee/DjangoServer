from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings

app_name = 'main'

urlpatterns = [
    path('', views.main, name = "main"),
]
