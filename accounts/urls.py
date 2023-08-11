from django.contrib import admin
from django.urls import path, include
from . import views
#from django.conf import settings

app_name = 'accounts'

urlpatterns = [
    path('Adv_Login/', views.Adv_Login, name = "Adv_Login"),
    path('Adv_Signup/', views.Adv_Signup, name = "Adv_SignUp"),
    path('Influ_Login/', views.Influ_Login, name = "Influ_Login"),
    path('Influ_Signup/', views.Influ_Signup, name = "Influ_SignUp"),
    path('MyPage/', views.MyPage, name = "MyPage"),
    path('AdvHome/', views.Adv_Logout, name = "Adv_Logout"),
    path('InfluHome/', views.Influ_Logout, name = "Influ_Logout"),
]
