from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', views.first_index, name = "first-index"),
    path('InfluHome/', views.InfluHome, name = "InfluHome"),
    path('AdvHome/', views.AdvHome, name = "AdvHome"),
    path('inner-page/', views.inner_page, name = "inner-page"),
    path('portfolio-details/', views.portfolio_details, name = "portfolio-details"),
    path('get_influencer_data', views.get_influencer_data, name='get_influencer_data'),
]
