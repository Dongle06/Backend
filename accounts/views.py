# # # # from msilib.schema import ServiceInstall
# # # from django.shortcuts import render, redirect
# # # from django.contrib.auth.models import User
# # # from django.contrib.auth import authenticate, login
# # # from rest_framework import viewsets

# # # def signup(request):
# # #     try:
# # #         user = User.objects.get(username=request.POST.get("UserId"))
# # #         messages.error(request, '이미 존재하는 아이디입니다.')

# # #         return redirect('signup')
# # #     except ObjectDoesNotExist :
# # #         user2 = User.objects.create_user(email=email, username=user_id, first_name=name, )

# # #     if request.method == 'POST':
# # #         if request.POST.get('password1') == request.POST.get('password2'):
# # #             user = User.objects.create_user(
# # #                 username=request.POST.get('UserId'),
# # #                 password=request.POST.get('Password1')
# # #             )
# # #             auth.login(request, user)
# # #             return redirect('home')
# # #     return render(request, 'signup.html')


# # # # class UserViewSet(viewsets.ModelViewSet):
# # # #     queryset = User.objects.all()
# # # #     serializer_class = UserSerializer

# # # from msilib.schema import ServiceInstall
# # # from os import stat

# from django.shortcuts import render 
# from rest_framework.decorators import api_view, permission_classes #api 
# from rest_framework import permissions
# from rest_framework.response import Response #api
# # from rest_framework import response
# from rest_framework import status

# # @api_view(['POST'])
# # @csrf_exempt
# # def log_in(request):
# #     if request.method == 'POST' :
# #         data = JSONParser().parse(request)
# #         search_email = data['email']
# #         obj = User.objects.get(email = search_email)

# #         if data['password'] == obj.password:
# #             return HttpResponse(status=200)

# #         else:
# #             return HttpResponse(status=400)


# # # from django.shortcuts import render 
# # # from rest_framework.decorators import api_view #api 
# # # from rest_framework.response import Response #api
# # # from rest_framework import status
# # # from django.http.response import HttpResponse

# # # @api_view(['GET'])
# # # def get(request) :
# # #     users = User.objects.all()
# # #     serialized_users=UserSerializer(users, many=True)
# # #     return Response(serialized_users.data)

# # # @api_view(['POST'])
# # # def post(request) :
# # #     if request.method == 'GET':
# # #         return HTTPResponse(status=200)
# # #     if request.method == 'POST' :
# # #         serializer= UserSerializer(data = request.data, many=True)
# # #         if(serializer.is_valid()):
# # #             serializer.save()
# # #             return Response(serializer.data, status=200)
# # #         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
# # #     return response(request)


# from django.contrib.auth.models import User
# from django.contrib import auth
# from django.http import response
# from rest_framework import status
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator

# @method_decorator(csrf_exempt)
# def signup(request) :
#     if request.method == "POST" :
#         if request.POST["password1"] == request.POST["password2"]:
#             user = User.objects.create_user(
#                 username = request.POST["username"], password = request.POST["password1"])
#             auth.login(request, user)
#             return response({"message": "ok"}, status=status.HTTP_201_CREATED)
#         return response({"message": "password is not indentical."}, status=status.HTTP_409_CONFLICT)
#     return response({"message": "not post."}, status=status.HTTP_400_BAD_REQUEST)


# @method_decorator(csrf_exempt)
# # @csrf_exempt
# def login(request) :
#     if request.mehtod == 'POST' :
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(request, username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return response({"message" : "ok"}, status=status.HTTP_200_OK)
#         else : 
#             return response({"error" : "username or password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
#     else : 
#         return response({"message" : "not post."})

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User
from .serializers import UserSerializer
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
import jwt, datetime
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny


@csrf_exempt
def account_list(request): #password1, password2가 일치하지 않을 때는 프론트단에서 바로 방지함 여기서 구현x
    if request.method == 'GET':
        query_set = User.objects.all()
        serializer = UserSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
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
            'id' : user.id,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat' : datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'JWT_SECRET', algorithm = 'HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key ='jwt', value= token, httponly=True) 
        response.data = {
            'jwt' : 'token'
        }

        # return Response()
        return JsonResponse({
            'jwt' : token
        })
        # if serializer.is_valid():
        #     return JsonResponse(serializer.data, status=200)
        # return JsonResponse(serializer.errors, status=400)

        # data = JSONParser().parse(request)
        # search_username = data['username']
        # obj = User.objects.get(username=search_username)

        # if data['password'] == obj.password:
        #     return HttpResponse(status=200)
        # else:
        #     return HttpResponse(status=400)

