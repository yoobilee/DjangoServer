from django.contrib import admin
from django.urls import path, include
from . import views
#from django.conf import settings

app_name = 'influencer'

urlpatterns = [
    path('Influencer1/', views.Influencer1, name = "Influencer1"),
]
