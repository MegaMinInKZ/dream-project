import django.contrib.auth.models
from django.db import models



# Create your models here.

class User(django.contrib.auth.models.AbstractUser):
    is_verified = models.BooleanField(default=False)
    has_shop = models.BooleanField(default=False)

class Shop(models.Model):
    passport_forward = models.ImageField()

