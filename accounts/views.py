
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User
from .serializers import UserSerializer, AuthSerializer,justSerializer
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
import jwt, datetime
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status

from accounts import serializers


@csrf_exempt
def account_list(request): #password1, password2가 일치하지 않을 때는 프론트단에서 바로 방지함 여기서 구현x
    if request.method == 'GET':
        query_set = User.objects.all()
        serializer = UserSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def signup(request): #password1, password2가 일치하지 않을 때는 프론트단에서 바로 방지함 여기서 구현x
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def account(request, pk):

    obj = User.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = UserSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    #회원 탈퇴
    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)

# @permission_classes([AllowAny])
# @api_view(('POST',))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_username = data['username']
        password = data['password']

        user = User.objects.filter(username=search_username).first()
        # serializer = UserSerializer(data=data)


        if user is None:
            raise AuthenticationFailed('User not found!') #log에만 뜸 json 결과로 안뜸
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!') #얘도

        payload= {
            'username' : user.username,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat' : datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, JWT_SECRET, algorithm = 'HS256').decode('utf-8')

        response = JsonResponse({
            'message' : 'ok'
        })

        response.set_cookie(key ='jwt', value= token, httponly=False) 

        return response
        

from pathlib import Path
import environ
import os

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

JWT_SECRET = env('JWT_SECRET')

@csrf_exempt
def authenticatedUser(request) :
    if request.method == 'GET' :
        token = request.COOKIES.get('jwt')

        if not token:
            response = JsonResponse({
                "isAuth" : "False"
            })
            return HttpResponse(response, status = status.HTTP_401_UNAUTHORIZED)   

        try :
            payload = jwt.decode(token, JWT_SECRET, algorithms= ['HS256'])

        except jwt.ExpiredSignatureError :
            response = JsonResponse(
                {
                    "isAuth" : "False"
                }
            )
            return HttpResponse(response, status = status.HTTP_401_UNAUTHORIZED)

        user = User.objects.filter(username = payload['username']).first()

        serializer = serializers.AuthSerializer(user)

        return JsonResponse(serializer.data, status = status.HTTP_200_OK)


@csrf_exempt
def logout(request) :
    if request.method == 'POST' :
        response = JsonResponse({
            "message" : "success"
        })
        response.delete_cookie('jwt')
        return response

