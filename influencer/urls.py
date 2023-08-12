from django.contrib import admin
from django.urls import path, include
from . import views
#from django.conf import settings

app_name = 'influencer'

urlpatterns = [
    path('Influencer1/', views.Influencer1, name = "Influencer1"),
    path('Influencer2/', views.Influencer2, name = "Influencer2"),
    path('Influencer3/', views.Influencer3, name = "Influencer3"),
    path('Influencer4/', views.Influencer4, name = "Influencer4"),
    path('Influencer5/', views.Influencer5, name = "Influencer5"),
    path('Influencer6/', views.Influencer6, name = "Influencer6"),
    path('Influencer7/', views.Influencer7, name = "Influencer7"),
    path('Influencer8/', views.Influencer8, name = "Influencer8"),
    path('Influencer9/', views.Influencer9, name = "Influencer9"),
]
