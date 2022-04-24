from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('register-user/', RegisterUserView.as_view(), name='register-user'),
    path('register-shop/', RegisterShopView.as_view(), name='register-shop'),
    path('verify-email/', VerifyUserEmail.as_view(), name='email-verify'),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    path('resend/token/', ResendEmailView.as_view(), name='resend-token')
]