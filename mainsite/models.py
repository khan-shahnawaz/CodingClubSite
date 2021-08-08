from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Navbar(models.Model):
    name=models.CharField(max_length=50)
    link=models.CharField(max_length=500)
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    cfid=models.CharField(max_length=100)
    cf_rating = models.IntegerField(default=0)
    batch=models.IntegerField(default=2020)
class slideshow(models.Model):
    caption = models.CharField(max_length=100)
    img=models.ImageField(upload_to='static/img')
    rank=models.IntegerField()