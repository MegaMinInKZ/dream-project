import django.contrib.auth.models
from django.db import models
from api.models import *



# Create your models here.

class User(django.contrib.auth.models.AbstractUser):
    is_verified = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='', null=True)

class Shop(models.Model):
    passport_forward = models.ImageField(upload_to='')
    passport_backward = models.ImageField(upload_to='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    slug = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='')
    city = models.ForeignKey(City, on_delete=models.CASCADE)
