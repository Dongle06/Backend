from rest_framework import serializers
from .models import User
# from django.core import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__') #모든 필드 사용 (사용하고자 하는 필드 입력하면 됨)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'password', 'nickname','email','created_at']
    user_id= serializers.CharField(max_length=15)
    password= serializers.CharField(max_length=20)
    nickname= serializers.CharField(max_length=15)
    email= serializers.CharField(max_length=30)
    created_at= serializers.DateTimeField(input_formats=["%Y-%m-%d"])
