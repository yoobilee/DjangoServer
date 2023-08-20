from django.db import models

# Create your models here.
class Keyword(models.Model):
    id=models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    words = models.CharField(max_length=100)
    weights = models.DecimalField(max_digits=15, decimal_places=10, primary_key=True)  # 소수점 10자리까지 저장

   
    class Meta:
        managed = False
        db_table = 'keyword'