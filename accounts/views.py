from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Influencer, Post_limmiae, Post_10_12_16yp, Post_b_saem, Post_wescsp1121, Post_vevi_d_live, Post_yakstory119, Post_iam_yaksa, Post_yakstagram, Post_pt_jjuny, User_adv, User_influ

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
            bussiness = request.POST['business']
        else:
            bussiness = ""  # 'business' 키가 없는 경우 빈 문자열로 설정
            
        # 'size' 키가 있는지 확인 후 값 가져오기
        if 'size' in request.POST:
            size = request.POST['size']
        else:
            size = ""  # 'size' 키가 없는 경우 빈 문자열로 설정

        user = User_adv(id=id, company=company, password=password, bussiness=bussiness, size=size)
        user.save()
        return redirect('accounts:Adv_Login') # 회원가입 후 로그인 페이지로 이동
    return render(request, 'Adv_Signup.html')

def Adv_Login(request):
    login_error = None  # 초기화

    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']

        try:
            user = User_adv.objects.get(id=id, password=password)
            # 로그인 성공 처리
            request.session['user_id'] = user.id
            return redirect('main:AdvHome')  # 로그인 후 광고주 홈으로 이동
        except User_adv.DoesNotExist:
            # 로그인 실패 처리
            login_error = "사용자가 존재하지 않습니다."  # 사용자 없음 메시지
        except User_adv.MultipleObjectsReturned:
            login_error = "여러 사용자가 존재합니다. 관리자에게 문의하세요."  # 중복 사용자 메시지
        else:
            login_error = "비밀번호가 틀렸습니다."  # 비밀번호 틀림 메시지

    return render(request, 'Adv_Login.html', {'login_error': login_error})


def Influ_Signup(request):
    if request.method == 'POST':
        id = request.POST['id']
        instagram_id = request.POST['instagram_id']
        password = request.POST['password']
        # 기타 필요한 데이터 수집
        
        # 'business' 키가 있는지 확인 후 값 가져오기
        if 'business' in request.POST:
            bussiness = request.POST['business']
        else:
            bussiness = ""  # 'business' 키가 없는 경우 빈 문자열로 설정
            
        # 'followers_count' 키가 있는지 확인 후 값 가져오기
        if 'followers_count' in request.POST:
            followers_count = request.POST['followers_count']
        else:
            followers_count = ""  # 'followers_count' 키가 없는 경우 빈 문자열로 설정

        user = User_influ(id=id, instagram_id=instagram_id, password=password, bussiness=bussiness, followers_count=followers_count)
        user.save()
        return redirect('accounts:Influ_Login')  # 회원가입 후 로그인 페이지로 이동
    return render(request, 'Influ_Signup.html')

def Influ_Login(request):
    login_error = None  # 초기화

    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']

        try:
            user = User_influ.objects.get(id=id, password=password)
            # 로그인 성공 처리
            request.session['user_id'] = user.id
            return redirect('main:InfluHome')  # 로그인 후 인플루언서 홈으로 이동
        except User_influ.DoesNotExist:
            # 로그인 실패 처리
            login_error = "사용자가 존재하지 않습니다."  # 사용자 없음 메시지
        except User_influ.MultipleObjectsReturned:
            login_error = "여러 사용자가 존재합니다. 관리자에게 문의하세요."  # 중복 사용자 메시지
        else:
            login_error = "비밀번호가 틀렸습니다."  # 비밀번호 틀림 메시지

    return render(request, 'Influ_Login.html', {'login_error': login_error})

def Adv_Logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('main:AdvHome')  # 로그아웃 후 광고주 홈으로 리다이렉트

def Influ_Logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('main:InfluHome')  # 로그아웃 후 인플루언서 홈으로 리다이렉트

def MyPage(request, user_type):
    user_id = request.session.get('user_id')
    if user_id:
        if user_type == 'adv':
            try:
                adv_user = User_adv.objects.get(id=user_id)
                context = {'user': adv_user}
                return render(request, 'MyPage.html', context)
            except User_adv.DoesNotExist:
                pass

        elif user_type == 'influ':
            try:
                influ_user = User_influ.objects.get(id=user_id)
                context = {'user': influ_user}
                return render(request, 'MyPage.html', context)
            except User_influ.DoesNotExist:
                pass

    # 유저 타입에 따른 정보가 없거나 로그인이 되어있지 않은 경우
    return render(request, 'MyPage_generic.html')