from django.urls import path
from .views import *

urlpatterns = [
    path('register-user/', RegisterUserView.as_view(), name='register-user'),
    path('register-shop/', RegisterShopView.as_view(), name='register-shop'),
    path('verify-email/', VerifyUserEmail.as_view(), name='email-verify')
]