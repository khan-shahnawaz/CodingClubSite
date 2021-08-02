from django.db import models

# Create your models here.
class Navbar(models.Model):
    name=models.CharField(max_length=50)
    link=models.CharField(max_length=500)