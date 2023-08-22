from django.db import models
from accounts.models import User_adv

# Create your models here.

class Recruitment(models.Model):
    agency = models.ForeignKey(User_adv, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    period = models.CharField(max_length=100)
    marketing_content = models.TextField()
    media_channels = models.TextField()
    subtitle = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    content_1 = models.TextField()
    sub_content_1 = models.TextField()
    content_2 = models.TextField()
    sub_content_2 = models.TextField()
    
    class Meta:
        managed = False
        db_table = 'Recruitment'

    
class RecruitmentImage(models.Model):
    recruitment = models.ForeignKey(Recruitment, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='recruitment_images/')
    is_profile = models.BooleanField(default=False)  # True if this image is for profile

    class Meta:
        managed = False
        db_table = 'RecruitmentImage'


class Hot_post(models.Model):
    post_id = models.CharField(max_length=100)
    comments_count = models.IntegerField()
    like_count = models.CharField(max_length=100)
    timestamp = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    insta_url = models.CharField(max_length=1000)
    post_url = models.CharField(max_length=1000, primary_key=True)
   
    class Meta:
        managed = False
        db_table = 'hot_post'


class Influencer_average(models.Model):
    goods_average = models.IntegerField()
    comments_average = models.IntegerField()
    followers_average = models.IntegerField()
    post_average = models.IntegerField()
    advpost_average = models.IntegerField()
    week_post_avg = models.IntegerField()
    number = models.IntegerField()
    ave_name = models.CharField(max_length=100)
    
    class Meta:
        managed = False
        db_table = 'influencer_average'