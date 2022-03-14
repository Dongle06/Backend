# # from msilib.schema import ServiceInstall
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
# # from django.http import HttpResponse
# from rest_framework import viewsets
# # from .serializer import UserSerializer
# # from .models import User

# # email = request.POST.get("e_mail")
# # name = request.POST.get("name")
# # user_id = request.POST.get("user_id")
# # user_pw = request.POST.get("user_pw")
# # profile_img_src = base_sql_data[0][0]

# def signup(request):
#     try:
#         user = User.objects.get(username=request.POST.get("UserId"))
#         messages.error(request, '이미 존재하는 아이디입니다.')

#         return redirect('signup')
#     except ObjectDoesNotExist :
#         user2 = User.objects.create_user(email=email, username=user_id, first_name=name, )

#     if request.method == 'POST':
#         if request.POST.get('password1') == request.POST.get('password2'):
#             user = User.objects.create_user(
#                 username=request.POST.get('UserId'),
#                 password=request.POST.get('Password1')
#             )
#             auth.login(request, user)
#             return redirect('home')
#     return render(request, 'signup.html')

# def login(request):
#     if request.method == 'POST':
#         username =request.POST.get('UserId')
#         password =request.POST.get('Password1')

#         user = auth.authenticate(
#             request, username=username, password=password
#         )

#         if user is not None:
#             auth.login(request, user)
#             return redirect('home')
#         else :
#             return render(request, 'login.html', {
#                 'error' : 'Username or Password is incorrect.',
#             })
#     else :
#         return render(request, 'login.html')
    
# def home(request):
#     return render(request, 'home.html')

# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         redirect('home')
#     return render(request, 'login.html')

# # class UserViewSet(viewsets.ModelViewSet):
# #     queryset = User.objects.all()
# #     serializer_class = UserSerializer

# # def say_hello(request):
# #     return render(request, 'hello.html', { 'name': "Mosh"})

# from msilib.schema import ServiceInstall
# from os import stat

from http.client import HTTPResponse
from django.http import HttpResponse, JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .serializers import UserSerializer
from rest_framework.parsers import JSONParser
from login import serializers
from django.shortcuts import render 
from rest_framework.decorators import api_view #api 
from rest_framework.response import Response #api

from rest_framework import status
from django.http.response import HttpResponse

@api_view(['POST'])
@csrf_exempt
# 계정 전체 조회(get), 회원가입(post)
def signup(request) :
    data = JSONParser().parse(request)
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# #pk로 특정 계정 조회(get), 수정(put), 삭제(delete)
# def account(request, pk):
#     obj = User.objects.get(pk=pk)

#     if request.method == 'GET' :
#         serializer = UserSerializer(obj)
#         return JsonResponse(serializer.data, safe = False)

#     elif request.method == 'PUT' :
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(obj, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE' :
#         obj.delete()
#         return HttpResponse(status=204)

@api_view(['POST'])
@csrf_exempt
def log_in(request):
    if request.method == 'POST' :
        data = JSONParser().parse(request)
        search_email = data['email']
        obj = User.objects.get(email = search_email)

        if data['password'] == obj.password:
            return HttpResponse(status=200)

        else:
            return HttpResponse(status=400)


# from django.shortcuts import render 
# from rest_framework.decorators import api_view #api 
# from rest_framework.response import Response #api

# from rest_framework import status
# from django.http.response import HttpResponse

# @api_view(['GET'])
# def get(request) :
#     users = User.objects.all()
#     serialized_users=UserSerializer(users, many=True)
#     return Response(serialized_users.data)

# @api_view(['POST'])
# def post(request) :
#     if request.method == 'GET':
#         return HTTPResponse(status=200)
#     if request.method == 'POST' :
#         serializer= UserSerializer(data = request.data, many=True)
#         if(serializer.is_valid()):
#             serializer.save()
#             return Response(serializer.data, status=200)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#     return response(request)