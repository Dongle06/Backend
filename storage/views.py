from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from storage.models import Storage
from storage.serializers import StorageSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes


@permission_classes([AllowAny])
@api_view(['GET', 'POST'])
@csrf_exempt
def storage_list(request, format=None): 
    if request.method == 'GET' :
        storage = Storage.objects.all()
        serializer = StorageSerializer(storage, many =True)
        return Response(serializer.data)
    
    elif request.method == 'POST' :
        serializer = StorageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@csrf_exempt
def findUsername(request, username):

    obj = Storage.objects.get(pk=username)

    if request.method == 'GET':
        serializer = StorageSerializer(obj)
        return Response(serializer.data)
