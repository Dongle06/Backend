from rest_framework import serializers
from .models import Storage

class StorageSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Storage
        fields = ('id', 'username', 'page', 'created')

    def create(self, validated_data):
        return Storage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.page = validated_data.get('page', instance.page)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
