from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from django.contrib.auth import logout
from accounts.models import Influencer, Keyword, Post_master, Post_10_12_16yp, Post_b_saem, Post_wescsp1121, Post_vevi_d_live, Post_yakstory119, Post_iam_yaksa, Post_yakstagram, Post_pt_jjuny, User_adv, User_influ
from django.core import serializers
from django.contrib.contenttypes.models import ContentType
from django.db.models import Avg
import logging
from .models import Recruitment, RecruitmentImage
from .forms import RecruitmentForm
from django.contrib.auth.decorators import login_required

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
            
            return render(request, 'InfluHome.html', {'user': user, 'influencer': influencer, 'first_keywords': first_keywords,
                                                      'second_keywords': second_keywords, 'third_keywords': third_keywords, 'forth_keywords': forth_keywords,
                                                      'fifth_keywords': fifth_keywords,'sixth_keywords': sixth_keywords})
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
            logger.info(user.business)
            
            return render(request, 'AgencyHome.html', {'user': user})
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
    user_id = request.session.get('user_id', None)  # 로그인된 사용자 아이디 가져오기
    
    if user_id:
        try:
            # 로그인한 사용자의 아이디로 User_adv 모델에서 해당 사용자의 정보를 가져옵니다.
            user = User_adv.objects.get(id=user_id)
            notices = Recruitment.objects.filter(agency=user)  # 해당 사용자의 공고 목록을 가져옵니다.
            return render(request, "notice-manage.html", {'user': user, 'notices': notices})
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
            
        return render(request, 'create_notice.html', {'form': form, 'user': user,'image': image})
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