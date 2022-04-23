from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import *


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailFiel(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        field = ('first_name', 'last_name', 'username',)
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

class RegisterShopSerializer(serializers.Serializer):
    owner_email = serializers.EmailFiel(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    owner_first_name = serializers.CharField(max_length=255)
    owner_last_name = serializers.CharField(max_length=255)
    owner_username = models.CharField(
        validators=[UnicodeUsernameValidator],
        max_length=150,
        unique=True,
        help_text=(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": ("A user with that username already exists."),
        },
    )
    class Meta:
        model = Shop
        fields = '__all__'
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        owner = User.objects.create(
            username=validated_data['owner_username'],
            first_name=validated_data['owner_first_name'],
            last_name=validated_data['owner_last_name'],
            email=validated_data['owner_email']
        )
        owner.set_password(validated_data['password'])
        owner.has_shop = True
        owner.save()
        shop = Shop.objects.create(
            passport_forward=validated_data['passport_forward'],
            passport_backward=validated_data['passport_backward'],
            user=owner,
            shop_name=validated_data['owner_email'],
            phone_number=validated_data['phone_number'],
            slug=validated_data['slug'],
            description=validated_data['description'],
            logo=validated_data['logo'],
            city=validated_data['city'],
        )
        shop.save()
