from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import *
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .util import *
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user_email = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user((user_email)).access_token
        current_site = get_current_site(request).domain
        relative_link = reverse('email-verify')
        absurl ='http://'+current_site+relative_link+'?token='+str(token)
        email_body = 'Hi, ' + user_email.username + ', use link to verify your email\n' + absurl
        data = {
            'domain': current_site,
            'email_subject': 'Verify your email',
            'email_body': email_body,
            'to_email': [user_email.email],
        }
        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)

class VerifyUserEmail(generics.GenericAPIView):
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, ['HS256'])
            user = User.objects.get(pk=payload['user_id'])
            user.is_verified=True
            user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as ident:
            return Response({'error': 'Activation expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as ident:
            return Response({'error': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)

class RegisterShopView(generics.CreateAPIView):
    queryset = Shop.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterShopSerializer

    def post(self, request):
        shop = request.data
        serializer = self.serializer_class(data=shop)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        shop_data=serializer.data
        user_email=Shop.objects.get(pk=shop_data['id']).user
        token = RefreshToken.for_user((user_email)).access_token
        current_site = get_current_site(request).domain
        relative_link = reverse('email-verify')
        absurl = 'http://' + current_site + relative_link + '?token=' + str(token)
        email_body = 'Hi, ' + user_email.username + ', use link to verify your email\n' + absurl
        data = {
            'domain': current_site,
            'email_subject': 'Verify your email',
            'email_body': email_body,
            'to_email': [user_email.email],
        }
        Util.send_email(data)
        return Response(shop_data, status=status.HTTP_201_CREATED)
# Create your views here.


