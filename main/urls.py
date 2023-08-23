from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', views.first_index, name = "first-index"),
    path('InfluHome/', views.InfluHome, name = "InfluHome"),
    path('AgencyHome/', views.AgencyHome, name = "AgencyHome"),
    path('TermOfUse_A/', views.TermOfUse_A, name = "TermOfUse_A"),
    path('PrivacyPolicy_A/', views.PrivacyPolicy_A, name = "PrivacyPolicy_A"),
    path('TermOfUse_I/', views.TermOfUse_I, name = "TermOfUse_I"),
    path('PrivacyPolicy_I/', views.PrivacyPolicy_I, name = "PrivacyPolicy_I"),
    path('get_influencer_data/', views.get_influencer_data, name='get_influencer_data'),
    path('get_additional_data/', views.get_additional_data, name='get_additional_data'),
    path('ComparisonAnalysis/', views.ComparisonAnalysis, name='ComparisonAnalysis'),
    path('DetailedAnalysis/', views.DetailedAnalysis, name='DetailedAnalysis'),
    path('DetailedAnalysisChart/', views.DetailedAnalysisChart, name='DetailedAnalysisChart'),
    path('notice/', views.notice, name='notice'),
    path('campaign/', views.campaign, name='campaign'),
    path('notice-Agency1/', views.notice_Agency1, name='notice-Agency1'),
    path('notice-Agency2/', views.notice_Agency2, name='notice-Agency2'),
    path('notice-Agency3/', views.notice_Agency3, name='notice-Agency3'),
    path('notice-manage/', views.notice_manage, name='notice-manage'),
    path('create/', views.create_notice, name='create_notice'),
    path('edit/<int:notice_id>/', views.edit_notice, name='edit_notice'),
    path('delete/<int:notice_id>/', views.delete_notice, name='delete_notice'),
    path('your-upload-view/', views.your_upload_view, name='your_upload_view'),
    path('serve-word2vec-model/', views.serve_word2vec_model, name='serve_word2vec_model'),
    path('InfluHome-base/', views.InfluHome_Base, name='InfluHome-Base'),
    path('AgencyHome_Base/', views.AgencyHome_Base, name='AgencyHome_Base'),
    path('agency_application/', views.agency_application, name='agency_application')
]
