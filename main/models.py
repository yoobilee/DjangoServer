from django.db import models

# Create your models here.

<<<<<<< HEAD
class YourModel(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title

=======
>>>>>>> 75c32d966ac65d5fc7bc9da71943e510d23aec00
# class Influencer(models.Model):
#   id = models.CharField(max_length=100, primary_key=True)
#   username = models.CharField(max_length=100)
#   biography = models.CharField(max_length=300)
#   media_count = models.IntegerField()
#   follows_count = models.IntegerField()
#   followers_count = models.IntegerField()
#   category = models.CharField(max_length=100)
#   adv_count = models.IntegerField()
#   week_avg_post = models.DecimalField(max_digits=5, decimal_places=1)
#   am_pm = models.CharField(max_length=100)
#   avg_post_time = models.CharField(max_length=100)
#   feed_percent = models.IntegerField()
#   reels_percent = models.IntegerField()
#   avg_comments = models.IntegerField()
#   avg_goods = models.IntegerField()
#   comments_percent = models.IntegerField()
#   goods_percent = models.IntegerField()
  
#   class Meta:
#     managed = False
#     db_table = 'influencers'
<<<<<<< HEAD

=======
>>>>>>> 75c32d966ac65d5fc7bc9da71943e510d23aec00
