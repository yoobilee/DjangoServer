from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from django.contrib.auth import logout
from accounts.models import Influencer, Keyword, Post_master, Post_10_12_16yp, Post_b_saem, Post_wescsp1121, Post_vevi_d_live, Post_yakstory119, Post_iam_yaksa, Post_yakstagram, Post_pt_jjuny, User_adv, User_influ
from django.core import serializers
from django.contrib.contenttypes.models import ContentType
from django.db.models import Avg
import logging
from .models import Recruitment, RecruitmentImage
from .models import Hot_post
from .forms import RecruitmentForm
from django.contrib.auth.decorators import login_required

from django.http import FileResponse
from django.conf import settings
import os
from django.views.decorators.csrf import csrf_exempt
from gensim.models import Word2Vec
import json

logger = logging.getLogger(__name__)

# Create your views here.

@csrf_exempt
def serve_word2vec_model(request):
    param = json.loads(request.body)
    keyword = param.get("keyword")
    user_id = param.get("user_id")
    
    # 모델 로드
    # 자기 경로 찾아서 입력!!!!
    model = Word2Vec.load('C:\\DjangoServer\\MA\\main\\static\\model\\'+user_id+'.model')  # 경로 구분자를 슬래시(/)로 사용하거나 역슬래시(\) 2개를 사용해야 함
    
    # 관련된 단어 찾기
    similar_words = model.wv.most_similar(keyword, topn=5)
    
    print(similar_words)
    
    if len(similar_words) == 5:
        first = similar_words[0][0]
        second = similar_words[1][0]
        third = similar_words[2][0]
        fourth = similar_words[3][0]
        fifth = similar_words[4][0]
    
    print(first)
    # 수정된 코드
    first_word = model.wv.most_similar(first, topn=3)
    second_word = model.wv.most_similar(second, topn=3)
    third_word =model.wv.most_similar(third, topn=3)
    fourth_word = model.wv.most_similar(fourth, topn=3)
    fifth_word = model.wv.most_similar(fifth, topn=3)
    
    print(first_word)
    
    return JsonResponse({'similar_words':similar_words, 'first':first_word, 'second':second_word, 'third':third_word, 'fourth':fourth_word, 'fifth':fifth_word})

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
            recruitment_queryset = Recruitment.objects.filter(agency_id=user_id)
            logger.info(user)
            influencer_queryset = Influencer.objects.filter(company=user.company)
             # 데이터셋 개수 계산
            recruitment_queryset_count = recruitment_queryset.count()
            influencer_queryset_count = influencer_queryset.count()
            context = {
                'recruitment_queryset_count': recruitment_queryset_count,
                'influencer_queryset_count': influencer_queryset_count,
                'user': user  # 'user' 정보도 context에 추가
            }

            return render(request, 'AgencyHome.html',context)
        except (User_adv.DoesNotExist):
            pass
    
    # 사용자가 로그인하지 않았거나 사용자 정보가 없는 경우 기본 템플릿을 렌더링합니다.
    return render(request, 'first-index.html')



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
        selected_influencer = Influencer.objects.get(username=influencer_username)
        
        selected_influencer_data = {
            '게시글 수': selected_influencer.media_count,
            '팔로워 수(백명)': selected_influencer.followers_count / 100,
            '팔로우 수': selected_influencer.follows_count,
            '평균 댓글 수': selected_influencer.avg_comments,
            '평균 좋아요 수': selected_influencer.avg_goods,
            '광고글 수': selected_influencer.adv_count,
            '주당 평균 게시글 수': selected_influencer.week_avg_post,
            '게시글 비율': selected_influencer.feed_percent,
            '릴스 비율': selected_influencer.reels_percent,
            '댓글 비율': selected_influencer.comments_percent,
            '좋아요 비율': selected_influencer.goods_percent,
        }
        
        return JsonResponse(selected_influencer_data)
    except Influencer.DoesNotExist:
        error_message = f"Influencer with username '{influencer_username}' does not exist."
        print("Error:", error_message)
        return JsonResponse({'error': error_message})
    except Exception as e:
        error_message = "An error occurred while fetching data."
        print("Error:", error_message, "Exception:", e)
        return JsonResponse({'error': error_message})


def ComparisonAnalysis(request):
    # 로그인한 사용자의 아이디를 가져옵니다.
    user_id = request.session.get('user_id', None)
    logger.info(user_id)
    if user_id:
        try:
            # 로그인한 사용자의 아이디로 User_influ 모델에서 해당 사용자의 정보를 가져옵니다.
            user = User_influ.objects.get(id=user_id)
            logger.info(user.id)
            # 로그인한 사용자의 아이디로 Influencer 모델에서 해당 사용자의 정보를 가져옵니다.
            login_influencer = Influencer.objects.get(username=user_id)
            logger.info(login_influencer.goods_percent)
            
            influencer = Influencer.objects.get(username=user_id)
            
            Influencer_list = list(Influencer.objects.values('username'))
            print(Influencer_list)
            return render(request, 'ComparisonAnalysis.html', {'user': user, 'influencer':influencer, 'login_influencer': login_influencer, 'Influencer_list' : Influencer_list})

        except (User_influ.DoesNotExist, Influencer.DoesNotExist):
            pass

    return render(request, "first-index.html")

def DetailedAnalysis(request):
    # 로그인한 사용자의 아이디를 가져옵니다.
    user_id = request.session.get('user_id', None)
    logger.info(user_id)
    if user_id:
        try:
            # 로그인한 사용자의 id로 User_adv 모델에서 해당 사용자의 정보를 가져옵니다.
            user = User_adv.objects.get(id=user_id)
            avg = Influencer.objects.get(company="회로의 챔피언들 평균")
            logger.info(avg.adv_count)
            # 로그인한 사용자의 company 값을 가져옵니다.
            user_company = user.company
            # 로그인한 사용자의 아이디로 Influencer 모델에서 해당 사용자의 정보를 가져옵니다.
            company_influencers_data = Influencer.objects.filter(company=user_company).values()   
            company_influencers_list = list(company_influencers_data)  # QuerySet을 리스트로 변환
            recruitment_queryset = Recruitment.objects.filter(agency_id=user_id)
            logger.info(user)
            influencer_queryset = Influencer.objects.filter(company=user.company)
             # 데이터셋 개수 계산
            recruitment_queryset_count = recruitment_queryset.count()
            influencer_queryset_count = influencer_queryset.count()
            context = {
                'recruitment_queryset_count': recruitment_queryset_count,
                'influencer_queryset_count': influencer_queryset_count,
                'user': user,  # 'user' 정보도 context에 추가
                'company_influencers_list': company_influencers_list,
                'avg': avg
            }
            company_influencers_avg_data = Influencer.objects.filter(company=user_company).annotate(
                avg_media_count=Avg('media_count'),
                avg_follower_count=Avg('followers_count'),
                avg_follow_count=Avg('follows_count'),
                avg_avg_comments=Avg('avg_comments'),
                avg_avg_goods=Avg('avg_goods'),
                avg_adv_count=Avg('adv_count'),
                avg_week_avg_post=Avg('week_avg_post'),
                avg_feed_percent=Avg('feed_percent'),
                avg_reels_percent=Avg('reels_percent'),
                avg_comments_percent=Avg('comments_percent'),
                avg_goods_percent=Avg('goods_percent')
            ).values()
            company_influencers_avg_data = list(company_influencers_avg_data)  # QuerySet을 리스트로 변환

            return render(request, 'DetailedAnalysis.html', context)

        except (User_adv.DoesNotExist, Influencer.DoesNotExist):
            pass

    return render(request, "first-index.html")

def notice_manage(request):
    user_id = request.session.get('user_id', None)  # 로그인된 사용자 아이디 가져오기
    
    if user_id:
        try:
            # 로그인한 사용자의 아이디로 User_adv 모델에서 해당 사용자의 정보를 가져옵니다.
            user = User_adv.objects.get(id=user_id)
            notices = Recruitment.objects.filter(agency=user)  # 해당 사용자의 공고 목록을 가져옵니다.
            recruitment_queryset = Recruitment.objects.filter(agency_id=user_id)
            logger.info(user)
            influencer_queryset = Influencer.objects.filter(company=user.company)
             # 데이터셋 개수 계산
            recruitment_queryset_count = recruitment_queryset.count()
            influencer_queryset_count = influencer_queryset.count()
            context = {
                'recruitment_queryset_count': recruitment_queryset_count,
                'influencer_queryset_count': influencer_queryset_count,
                'user': user,  # 'user' 정보도 context에 추가
                'notices': notices
            }
            return render(request, "notice-manage.html", context)
        except User_adv.DoesNotExist:
            pass
    
    # 사용자가 로그인하지 않았거나 사용자 정보가 없는 경우 기본 템플릿을 렌더링합니다.
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

def notice_list(request):
    notices = Recruitment.objects.all()  # 공고 목록을 가져옵니다.
    return render(request, 'notice_list.html', {'notices': notices})

def create_notice(request):
    user_id = request.session.get('user_id', None)
  
    if user_id:
        user = User_adv.objects.get(id=user_id)
        
        if request.method == 'POST':
            form = RecruitmentForm(request.POST, request.FILES)
            
            if form.is_valid():
                recruitment = form.save(commit=False, user=user)
                recruitment.agency = user  # 현재 로그인된 사용자(User_adv 인스턴스)를 agency로 설정
                recruitment.save()
                
                profile_image = form.cleaned_data['profile_image']
                profile_image_instance = RecruitmentImage.objects.create(recruitment=recruitment, image=profile_image, is_profile=True)
                
                content_images = request.FILES.getlist('content_images')
                for image in content_images:
                    RecruitmentImage.objects.create(recruitment=recruitment, image=image, is_profile=False)
                
                return redirect('/notice-manage/')
        else:
            form = RecruitmentForm()
            
        return render(request, 'create_notice.html', {'form': form, 'user': user})
    else:
        # 로그인되지 않은 경우에 대한 처리
        return redirect('accounts:Adv_Login')     # 로그인 페이지로 리디렉션
    
def edit_notice(request, notice_id):
    notice = get_object_or_404(Recruitment, pk=notice_id)
    
    if request.method == 'POST':
        # Handle form submission and notice editing logic here
        # ...
        return redirect('/notice-manage/')  # 공고 수정 후 관리 페이지로 리디렉션
    
    return render(request, 'edit_notice.html', {'notice': notice})

def delete_notice(request, notice_id):
    notice = get_object_or_404(Recruitment, pk=notice_id)
    
    if request.method == 'POST':
        notice.delete()  # 공고 삭제
        return redirect('/notice-manage/')  # 관리 페이지로 리디렉션
    
    return redirect('/notice-manage/')  # 삭제 확인 페이지 없이 바로 관리 페이지로 리디렉션

def your_upload_view(request):
    if request.method == 'POST' and request.FILES['content_images']:
        uploaded_file = request.FILES['content_images']
        
        # 파일을 저장하고 데이터베이스에 연결
        recruitment_image = RecruitmentImage.objects.create(image=uploaded_file, is_profile=False)
        
        response_data = {'message': 'File uploaded successfully', 'image_id': recruitment_image.id}
        return JsonResponse(response_data)
    else:
        response_data = {'message': 'File upload failed'}
        return JsonResponse(response_data, status=400)
    
def search_influencers(request):
    search_term = request.GET.get("search", "")
    
    if search_term:
        influencers = Influencer.objects.filter(username__icontains=search_term)
    else:
        influencers = Influencer.objects.all()
    
    return render(request, "search.html", {"influencers": influencers})

def InfluHome_Base(request):
    # 로그인한 사용자의 아이디를 가져옵니다.
    user_id = request.session.get('user_id', None)
    
    if user_id:
        try:
            # 로그인한 사용자의 아이디로 Influencer 모델에서 해당 사용자의 정보를 가져옵니다.
            avg = Influencer.objects.get(company="회로의 챔피언들 평균")

            # 컨텍스트에 avg 변수를 추가하여 해당 변수를 템플릿에서 사용할 수 있도록 합니다.
            avg = {'avg': avg}
            
            return render(request, 'InfluHome-Base.html', avg)
        except Influencer.DoesNotExist:
            pass

    return render(request, "first-index.html")


def AgencyHome_Base(request):
    # 로그인한 사용자의 아이디를 가져옵니다.
    user_id = request.session.get('user_id', None)
    
    if user_id:
        try:
            # 로그인한 사용자의 아이디로 Influencer 모델에서 해당 사용자의 정보를 가져옵니다.
            user = User_adv.objects.get(id=user_id)
            login_influencer = Influencer.objects.get(username=user_id)
            logger.info(login_influencer.goods_percent)

            # 컨텍스트에 login_influencer 변수를 추가하여 해당 변수를 템플릿에서 사용할 수 있도록 합니다.
            
            recruitment_queryset = Recruitment.objects.filter(agency_id=user_id)
            logger.info(user)
            influencer_queryset = Influencer.objects.filter(company=user.company)
             # 데이터셋 개수 계산
            recruitment_queryset_count = recruitment_queryset.count()
            influencer_queryset_count = influencer_queryset.count()
            context = {
                'recruitment_queryset_count': recruitment_queryset_count,
                'influencer_queryset_count': influencer_queryset_count,
                'user': user,# 'user' 정보도 context에 추가
                'login_influencer': login_influencer
            }
            
            return render(request, 'AgencyHome-Base.html', context)
        except Influencer.DoesNotExist:
            pass

    return render(request, "first-index.html")