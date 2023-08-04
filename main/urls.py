from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings

app_name = 'main'

urlpatterns = [
    path('', views.base, name = "base"),
    path('inner-page/', views.inner_page, name = "inner-page"),
    path('portfolio-details/', views.portfolio_details, name = "portfolio-details"),
]
