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
    path('portfolio-details/<int:pk>/', views.portfolio_details, name='portfolio-details'),
    path('portfolio-details01/', views.portfolio_details01, name = "portfolio-details01"),
    path('TermOfUse_A/', views.TermOfUse_A, name = "TermOfUse_A"),
    path('PrivacyPolicy_A/', views.PrivacyPolicy_A, name = "PrivacyPolicy_A"),
    path('TermOfUse_I/', views.TermOfUse_I, name = "TermOfUse_I"),
    path('PrivacyPolicy_I/', views.PrivacyPolicy_I, name = "PrivacyPolicy_I"),
    path('get_influencer_data', views.get_influencer_data, name='get_influencer_data'),
]
