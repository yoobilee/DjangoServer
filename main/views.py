from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from django.contrib.auth import logout
from accounts.models import Influencer, Keyword, Post_master, Post_10_12_16yp, Post_b_saem, Post_wescsp1121, Post_vevi_d_live, Post_yakstory119, Post_iam_yaksa, Post_yakstagram, Post_pt_jjuny, User_adv, User_influ
from django.core import serializers
from django.contrib.contenttypes.models import ContentType
from django.db.models import Avg
import logging
from .models import Hot_post

logger = logging.getLogger(__name__)

# Create your views here.
def first_index(request):
    logout(request)
    return render(request, "first-index.html")


def InfluHome(request):
    # 로그인한 사용자의 아이디를 가져옵니다.
    user_id = request.session.get('user_id', None)
    
    if user_id:
        try:
            # 로그인한 사용자의 아이디로 User_influ 모델에서 해당 사용자의 정보를 가져옵니다.
            user = User_influ.objects.get(id=user_id)
            
            # 로그인한 사용자의 아이디로 Influencer 모델에서 해당 사용자의 정보를 가져옵니다.
            influencer = Influencer.objects.get(username=user_id)
            first_keywords = Keyword.objects.filter(username=user_id).first()
            second_keywords = Keyword.objects.filter(username=user_id)[1]
            third_keywords = Keyword.objects.filter(username=user_id)[2]
            forth_keywords = Keyword.objects.filter(username=user_id)[3]
            fifth_keywords = Keyword.objects.filter(username=user_id)[4]
            sixth_keywords = Keyword.objects.filter(username=user_id).last()
            
            hot_post1 = Hot_post.objects.filter(username=user_id)[0]
            hot_post2 = Hot_post.objects.filter(username=user_id)[1]
            hot_post3 = Hot_post.objects.filter(username=user_id)[2]
            hot_post4 = Hot_post.objects.filter(username=user_id)[3]
            
    
            return render(request, 'InfluHome.html', {'user': user, 'influencer': influencer, 'first_keywords': first_keywords,
                                                      'second_keywords': second_keywords, 'third_keywords': third_keywords, 'forth_keywords': forth_keywords,
                                                      'fifth_keywords': fifth_keywords,'sixth_keywords': sixth_keywords, 'hot_post1': hot_post1,
                                                      'hot_post2': hot_post2,'hot_post3': hot_post3,'hot_post4': hot_post4})
        except (User_influ.DoesNotExist, Influencer.DoesNotExist):
            pass
    
    # 사용자가 로그인하지 않았거나 사용자 정보가 없는 경우 기본 템플릿을 렌더링합니다.
    return render(request, 'InfluHome.html')



def AgencyHome(request):
    # 로그인한 사용자의 아이디를 가져옵니다.
    user_id = request.session.get('user_id', None)
    
    if user_id:
        try:
            # 로그인한 사용자의 아이디로 User_adv 모델에서 해당 사용자의 정보를 가져옵니다.
            user = User_adv.objects.get(id=user_id)
            
            # 로그인한 사용자의 아이디로 Influencer 모델에서 해당 사용자의 정보를 가져옵니다.
            influencer = Influencer.objects.get(id=user_id)
            
            return render(request, 'AgencyHome.html', {'user': user, 'influencer': influencer})
        except (User_adv.DoesNotExist, Influencer.DoesNotExist):
            pass
    
    # 사용자가 로그인하지 않았거나 사용자 정보가 없는 경우 기본 템플릿을 렌더링합니다.
    return render(request, 'AgencyHome.html')



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

def ComparisonAnalysis(request):
    # 로그인한 사용자의 아이디를 가져옵니다.
    user_id = request.session.get('user_id', None)
    
    if user_id:
        try:
            # 로그인한 사용자의 아이디로 User_influ 모델에서 해당 사용자의 정보를 가져옵니다.
            user = User_influ.objects.get(id=user_id)
            
            # 로그인한 사용자의 아이디로 Influencer 모델에서 해당 사용자의 정보를 가져옵니다.
            influencer = Influencer.objects.get(username=user_id)
            
            return render(request, 'ComparisonAnalysis.html', {'user': user, 'influencer': influencer})
        except (User_influ.DoesNotExist, Influencer.DoesNotExist):
            pass

    return render(request, "ComparisonAnalysis.html")

def DetailedAnalysis(request):
    return render(request, "DetailedAnalysis.html")

def notice_manage(request):
    return render(request, "notice-manage.html")

def notice(request):
    # 로그인한 사용자의 아이디를 가져옵니다.
    user_id = request.session.get('user_id', None)
    
    if user_id:
        try:
            # 로그인한 사용자의 아이디로 User_influ 모델에서 해당 사용자의 정보를 가져옵니다.
            user = User_influ.objects.get(id=user_id)
            
            # 로그인한 사용자의 아이디로 Influencer 모델에서 해당 사용자의 정보를 가져옵니다.
            influencer = Influencer.objects.get(username=user_id)
            
            return render(request, 'notice.html', {'user': user, 'influencer': influencer})
        except (User_influ.DoesNotExist, Influencer.DoesNotExist):
            pass

    return render(request, "notice.html")

def notice_Agency1(request):
    # 로그인한 사용자의 아이디를 가져옵니다.
    user_id = request.session.get('user_id', None)
    
    if user_id:
        try:
            # 로그인한 사용자의 아이디로 User_influ 모델에서 해당 사용자의 정보를 가져옵니다.
            user = User_influ.objects.get(id=user_id)
            
            # 로그인한 사용자의 아이디로 Influencer 모델에서 해당 사용자의 정보를 가져옵니다.
            influencer = Influencer.objects.get(username=user_id)
            
            return render(request, 'notice-Agency1.html', {'user': user, 'influencer': influencer})
        except (User_influ.DoesNotExist, Influencer.DoesNotExist):
            pass

    return render(request, "notice-Agency1.html")