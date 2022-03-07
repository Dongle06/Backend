# from xml.etree.ElementInclude import include
from django.urls import include, path
from django.contrib.auth import views as auth_views
# from rest_framework import routers
from . import views

# app_name = 'login'

# router = routers.DefaultRouter() #defaultRouter 설정
# router.register('user', views.UserViewSet) #ViewSet과 함께 user라는 router 등록

# urlpatterns = [
#     path('', include(router.urls)),
# ]
urlpatterns = [
    path('signup/',views.signup, name='signup'), #회원가입
    path('', views.login, name='login'), #로그인
    path('home/', views.home, name = 'home'), #로그인 성공하면 뜨는 url
    path('logout/', views.logout, name = 'logout'),
]