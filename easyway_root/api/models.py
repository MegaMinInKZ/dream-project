from django.db import models
from account.models import *
from django.core.validators import MaxValueValidator, MinValueValidator

class City(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    class Meta:
        verbose_name_plural = 'Cities'

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    class Meta:
        verbose_name_plural = 'Categories'
class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    upload_date = models.DateField(auto_now_add=True)
    slug = models.CharField(max_length=250, unique=True)
    discount = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(100),
    ])