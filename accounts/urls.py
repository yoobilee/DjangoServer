from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
#from django.conf import settings

app_name = 'accounts'

urlpatterns = [
    path('Adv_Login/', views.Adv_Login, name = "Adv_Login"),
    path('Adv_Signup/', views.Adv_Signup, name = "Adv_Signup"),
    path('Influ_Login/', views.Influ_Login, name = "Influ_Login"),
    path('Influ_Signup/', views.Influ_Signup, name = "Influ_Signup"),
    path('MyPage/', views.MyPage, name = "MyPage"),
    path('Adv_Logout/', auth_views.LogoutView.as_view(next_page='main:first-index'), name='Adv_Logout'),
    path('Influ_Logout/', auth_views.LogoutView.as_view(next_page='main:first-index'), name='Influ_Logout'),
    
]