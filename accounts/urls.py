from django.contrib import admin
from django.urls import path, include
from . import views
#from django.conf import settings

app_name = 'accounts'

urlpatterns = [
    path('Adv_Login/', views.Adv_Login, name = "Adv_Login"),
    path('Influ_Login/', views.Influ_Login, name = "Influ_Login"),
]
