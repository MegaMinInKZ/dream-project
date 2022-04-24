from django.urls import path
from .views import *

urlpatterns = [
    path('category/<slug:slug>/', CategoryView.as_view()),
    path('categoryList/', CategoryListView.as_view()),
    path('cityList/', CityListView.as_view()),
    path('city/<slug:slug>/', CityView.as_view()),
    path('product/<slug:slug>/', ProductRetrieveView.as_view()),
]