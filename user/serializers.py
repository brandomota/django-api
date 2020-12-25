from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'cpf']


class UserCreationSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=255)
    email = serializers.CharField(required=True, max_length=100)
    cpf = serializers.CharField(required=True, max_length=14, min_length=14, help_text='format: xxx.xxx.xxx-xx')
    password = serializers.CharField(required=True)


class LoginSerializer(serializers.Serializer):
    login = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)