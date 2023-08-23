from django import forms
from .models import Recruitment
from .models import Supply_influencer


class RecruitmentForm(forms.ModelForm):
    profile_image = forms.ImageField(label='프로필 이미지 업로드')
    content_images = forms.ImageField(label='본문 이미지 업로드')

    class Meta:
        model = Recruitment
        fields = '__all__'
        labels = {
            'title': '공고 제목',
            'period': '모집 기간',
            'marketing_content': '마케팅 진행내용',
            'media_channels': '진행 매체',
            'subtitle': '부제목',
            'category': '카테고리',
            'content_1': '본문 내용 1',
            'sub_content_1': '보조 내용 1',
            'content_2': '본문 내용 2',
            'sub_content_2': '보조 내용 2',
        }

    def save(self, commit=True, user=None):
        instance = super(RecruitmentForm, self).save(commit=False)
        if user is not None:
            instance.agency = user  # 전달된 user 정보를 사용하여 agency 설정
        if commit:
            instance.save()
        return instance
    
class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply_influencer
        fields = ['name', 'username', 'email', 'phone_num', 'reason_supply']