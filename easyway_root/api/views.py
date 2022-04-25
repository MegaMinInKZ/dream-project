from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import *
from .serializers import *

# Create your views here.


class ShopListView(ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ShopView(ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        shop = Shop.objects.get(slug=self.kwargs['slug'])
        return Product.objects.filter(shop=shop)

class ProductRetrieveView(RetrieveAPIView):
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    queryset = Product.objects.all()

class CategoryView(ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        cat = Category.objects.get(slug=self.kwargs['slug'])
        return Product.objects.filter(category=cat)

class CityListView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityView(ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        city = City.objects.get(slug=self.kwargs['slug'])
        return Product.objects.filter(city=city)


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer