from rest_framework import serializers
from .models import *


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['title', 'slug']

class ShopSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = Shop
        fields = ['shop_name', 'phone_number', 'slug', 'description', 'logo', 'city']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    city = CitySerializer()
    shop = ShopSerializer()
    class Meta:
        model = Product
        fields = '__all__'
        lookup_field = 'slug'



