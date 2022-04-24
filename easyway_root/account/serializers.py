from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import *


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ("username", "password", "password2", "email", "first_name", "last_name")
        extra_kwargs={
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Password fields didn't match."})
        return attrs
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class RegisterShopSerializer(serializers.ModelSerializer):
    user = RegisterUserSerializer()
    class Meta:
        model = Shop
        fields = (
            'user', 'passport_forward', 'passport_backward', 'shop_name', 'phone_number', 'slug', 'description', 'logo',
            'city', 'id'
        )
    def validate(self, attrs):
        if attrs['user']['password'] != attrs['user']['password2']:
            raise serializers.ValidationError({'password': "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        owner = User.objects.create(
            username=validated_data['user']['username'],
            first_name=validated_data['user']['first_name'],
            last_name=validated_data['user']['last_name'],
            email=validated_data['user']['email']
        )
        owner.set_password(validated_data['user']['password'])
        owner.has_shop = True
        owner.save()
        shop = Shop.objects.create(
            passport_forward=validated_data['passport_forward'],
            passport_backward=validated_data['passport_backward'],
            user=owner,
            shop_name=validated_data['shop_name'],
            phone_number=validated_data['phone_number'],
            slug=validated_data['slug'],
            description=validated_data['description'],
            logo=validated_data['logo'],
            city=validated_data['city'],
        )
        shop.save()
        return shop
class ResendEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']
    def validate(self, attrs):
        user = User.objects.get(email=attrs['email'])
        if not user:
            raise serializers.ValidationError({'email': "User with this email doesn't exist"})
        if user.is_verified:
            raise serializers.ValidationError({'email': "User already confirmed email"})
        return user
