from rest_framework import serializers
from .models import Account
# from django.core import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username','email', 'password', 'created_at']
    # user_id= serializers.CharField(max_length=15)
    # password= serializers.CharField(max_length=20)
    # email= serializers.CharField(max_length=30)
    # # created_at= serializers.DateTimeField(input_formats=["%Y-%m-%d"])
