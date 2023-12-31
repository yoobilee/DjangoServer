from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Influencer, Post_10_12_16yp, Post_b_saem, Post_wescsp1121, Post_vevi_d_live, Post_yakstory119, Post_iam_yaksa, Post_yakstagram, Post_pt_jjuny, User_adv, User_influ

# Create your views here.

# your_app/views.py

def Adv_Signup(request):
    if request.method == 'POST':
        id = request.POST['id']
        company = request.POST['company']
        password = request.POST['password']
        # 기타 필요한 데이터 수집
        
        # 'business' 키가 있는지 확인 후 값 가져오기
        if 'business' in request.POST:
            business = request.POST['business']
        else:
            business = ""  # 'business' 키가 없는 경우 빈 문자열로 설정
            
        # 'size' 키가 있는지 확인 후 값 가져오기
        if 'size' in request.POST:
            size = request.POST['size']
        else:
            size = ""  # 'size' 키가 없는 경우 빈 문자열로 설정

        user = User_adv(id=id, company=company, password=password, business=business, size=size)
        user.save()
        return redirect('accounts:Adv_Login') # 회원가입 후 로그인 페이지로 이동
    return render(request, 'Adv_Signup.html')

def Adv_Login(request):
    login_error = None

    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']

        try:
            user = User_adv.objects.get(id=id, password=password)
            request.session['user_id'] = user.id
            request.session['user_type'] = 'adv'  # 유형 정보를 세션에 저장
            if 'login_referer' in request.session:
                referer = request.session.pop('login_referer')
                return redirect(referer)
            else:
                return redirect('main:AgencyHome')
        except User_adv.DoesNotExist:
            login_error = "사용자가 존재하지 않습니다."
        except User_adv.MultipleObjectsReturned:
            login_error = "여러 사용자가 존재합니다. 관리자에게 문의하세요."
        else:
            login_error = "비밀번호가 틀렸습니다."

    return render(request, 'Adv_Login.html', {'login_error': login_error})



def Influ_Signup(request):
    if request.method == 'POST':
        id = request.POST['id']
        instagram_id = request.POST['instagram_id']
        password = request.POST['password']
        # 기타 필요한 데이터 수집
        
        # 'business' 키가 있는지 확인 후 값 가져오기
        if 'business' in request.POST:
            business = request.POST['business']
        else:
            business = ""  # 'business' 키가 없는 경우 빈 문자열로 설정
            
        # 'followers_count' 키가 있는지 확인 후 값 가져오기
        if 'followers_count' in request.POST:
            followers_count = request.POST['followers_count']
        else:
            followers_count = ""  # 'followers_count' 키가 없는 경우 빈 문자열로 설정

        user = User_influ(id=id, instagram_id=instagram_id, password=password, business=business, followers_count=followers_count)
        user.save()
        return redirect('accounts:Influ_Login') # 회원가입 후 로그인 페이지로 이동
    return render(request, 'Influ_Signup.html')


def Influ_Login(request):
    login_error = None

    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']

        try:
            user = User_influ.objects.get(id=id, password=password)
            request.session['user_id'] = user.id
            request.session['user_type'] = 'influ'  # 유형 정보를 세션에 저장
            if 'login_referer' in request.session:
                referer = request.session.pop('login_referer')
                return redirect(referer)
            else:
                return redirect('main:InfluHome')
        except User_influ.DoesNotExist:
            login_error = "사용자가 존재하지 않습니다."
        except User_influ.MultipleObjectsReturned:
            login_error = "여러 사용자가 존재합니다. 관리자에게 문의하세요."
        else:
            login_error = "비밀번호가 틀렸습니다."

    return render(request, 'Influ_Login.html', {'login_error': login_error})

def InfluHome(request):
    return render(request, 'InfluHome.html')





def Adv_Logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('main:first-index')  # 로그아웃 후 메인 홈으로 리다이렉트

def Influ_Logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('main:first-index')  # 로그아웃 후 메인 홈으로 리다이렉트


def get_user_type(user):
    if isinstance(user, User_adv):
        return 'adv'
    elif isinstance(user, User_influ):
        return 'influ'
    else:
        return 'unknown'
