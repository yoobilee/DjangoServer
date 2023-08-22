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