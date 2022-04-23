from django.db import models

class City(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
