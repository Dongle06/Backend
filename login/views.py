# from msilib.schema import ServiceInstall
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# from django.http import HttpResponse
from rest_framework import viewsets
# from .serializer import UserSerializer
# from .models import User

email = request.POST.get("e_mail")
name = request.POST.get("name")
user_id = request.POST.get("user_id")
user_pw = request.POST.get("user_pw")
profile_img_src = base_sql_data[0][0]

def signup(request):
    try:
        user = User.objects.get(username=request.POST.get("UserId"))
        messages.error(request, '이미 존재하는 아이디입니다.')

        return redirect('signup')
    except ObjectDoesNotExist :
        user2 = User.objects.create_user(email=email, username=user_id, first_name=name, )

    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            user = User.objects.create_user(
                username=request.POST.get('UserId'),
                password=request.POST.get('Password1')
            )
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username =request.POST.get('UserId')
        password =request.POST.get('Password1')

        user = auth.authenticate(
            request, username=username, password=password
        )

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else :
            return render(request, 'login.html', {
                'error' : 'Username or Password is incorrect.',
            })
    else :
        return render(request, 'login.html')
    
def home(request):
    return render(request, 'home.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        redirect('home')
    return render(request, 'login.html')

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# def say_hello(request):
#     return render(request, 'hello.html', { 'name': "Mosh"})