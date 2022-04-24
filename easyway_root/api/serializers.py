from rest_framework import serializers
from .models import *


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['title', 'slug']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        lookup_field = 'slug'
        depth = 1



