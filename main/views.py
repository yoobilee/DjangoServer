from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from django.contrib.auth import logout
from .models import YourModel
from accounts.models import Influencer, Post_master, Post_10_12_16yp, Post_b_saem, Post_wescsp1121, Post_vevi_d_live, Post_yakstory119, Post_iam_yaksa, Post_yakstagram, Post_pt_jjuny, User_adv, User_influ
from django.core import serializers
from django.contrib.contenttypes.models import ContentType
from django.db.models import Avg

# Create your views here.
def first_index(request):
    logout(request)
    return render(request, "first-index.html")

def InfluHome(request):
    return render(request, "InfluHome.html")

def AgencyHome(request):
    influencers = Influencer.objects.all()    
    return render(request, 'AgencyHome.html', {'influencers': influencers})

def inner_page(request):
    return render(request, "inner-page.html")

def portfolio_details01(request):
    return render(request, "portfolio-details01.html")

def TermOfUse_A(request):
    return render(request, "TermOfUse_A.html")

def PrivacyPolicy_A(request):
    return render(request, "PrivacyPolicy_A.html")

def TermOfUse_I(request):
    return render(request, "TermOfUse_I.html")

def PrivacyPolicy_I(request):
    return render(request, "PrivacyPolicy_I.html")

from django.http import JsonResponse

def get_influencer_data(request):
    influencer_name = request.GET.get('influencer', None)
    
    try:
        influencer = Influencer.objects.get(username=influencer_name)
        
        influencer_data = {
            '게시글 수': influencer.media_count,
            '팔로워 수': influencer.followers_count,
            '팔로우 수': influencer.follows_count,
            # ... 추가 필드들
        }
        
        # ContentType으로 모델명 추출
        influencer_content_type = ContentType.objects.get_for_model(influencer)
        model_name = influencer_content_type.model
        
        # 해당 모델명을 가진 Post 데이터 가져오기
        post_model = ContentType.objects.get(model=model_name)
        post_data = post_model.model_class().objects.filter(username=influencer_name)
        print(comments_count_sum)
        comments_count_sum = post_data.aggregate(Avg('comments_count'))['comments_count__avg']
        like_count_sum = post_data.aggregate(Avg('like_count'))['like_count__avg']
        influencer_data['평균 댓글 수'] = comments_count_sum
        influencer_data['평균 좋아요 수'] = like_count_sum
        print(1111111)
        print(influencer_data)
        return JsonResponse(influencer_data)
    except Influencer.DoesNotExist:
        return JsonResponse({'error': 'Influencer not found'})
    
    
def get_additional_data(request):
    influencer_username = request.GET.get('username', None)
    
    try:
        influencer = Influencer.objects.get(username=influencer_username)
        comments_count_sum = int(Post_master.objects.filter(username=influencer_username).aggregate(Avg('comments_count'))['comments_count__avg'])
        like_count_sum = int(Post_master.objects.filter(username=influencer_username).aggregate(Avg('like_count'))['like_count__avg'])


        
        influencer_data = {
            '게시글 수': influencer.media_count,
            '팔로워 수': influencer.followers_count,
            '팔로우 수': influencer.follows_count,
            '댓글 수': comments_count_sum,
            '좋아요 수': like_count_sum,
        }
        
        return JsonResponse(influencer_data)
    except (Influencer.DoesNotExist, Post_master.username.DoesNotExist):
        return JsonResponse({'error': 'Data not found'})
    
def notice_manage(request):
    return render(request, "notice-manage.html")

def notice(request):
    return render(request, "notice.html")

def notice_Agency1(request):
    return render(request, "notice-Agency1.html")