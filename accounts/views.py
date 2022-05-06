
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

        token = jwt.encode(payload, 'JWT_SECRET', algorithm = 'HS256').decode('utf-8')

        response = JsonResponse({
            'message' : 'ok'
        })

        response.set_cookie(key ='jwt', value= token, httponly=True) 

        return response
        # return JsonResponse({
        #     'jwt' : token
        # })
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

@csrf_exempt
def authenticatedUser(request) :
    if request.method == 'GET' :
        token = request.COOKIES.get('jwt')

        # if not token:
        #     raise AuthenticationFailed('Unauthenticated!')

        # try :
        #     payload = jwt.decode(token, 'JWT_SECRET', algorithm = ['HS256'])
        
        # except jwt.ExpiredSignatureError :
        #     raise AuthenticationFailed('Unauthenticated!')
        
        # user = User.objects.filter(id = payload['id']).first()
        # serializer = UserSerializer(user)

        return JsonResponse({
            'jwt' : token
        })

@csrf_exempt
def logout(request) :
    if request.method == 'POST' :
        response = HttpResponse("bye")
        response.delete_cookie('jwt')
        return response
