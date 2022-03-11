from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__') #모든 필드 사용 (사용하고자 하는 필드 입력하면 됨)