from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings

app_name = 'accounts'

urlpatterns = [
    path('agency_signup/', views.agency_signup, name = "agency_signup"),
    path('influencer_signup/', views.influencer_signup, name = "influencer_signup"),
]
