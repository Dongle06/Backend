# # from xml.etree.ElementInclude import include
# from django.urls import include, path
# from django.contrib.auth import views as auth_views
# # from rest_framework import routers
# from . import views

# # app_name = 'login'

# # router = routers.DefaultRouter() #defaultRouter 설정
# # router.register('user', views.UserViewSet) #ViewSet과 함께 user라는 router 등록

# # urlpatterns = [
# #     path('', include(router.urls)),
# # ]
# urlpatterns = [
#     path('accounts/',views.account_list, name='signup'), #회원가입
#     path('login/', views.login, name='login'), #로그인
#     # path('home/', views.home, name = 'home'), #로그인 성공하면 뜨는 url
#     # path('logout/', views.logout, name = 'logout'),
#     path('accounts/<int:pk>', views.account),
#     path('auth/', include('rest_framework.urls', namespace='rest_framework')),
# ]

from django.urls import path
from accounts import views
from django.conf.urls import include

app_name = 'accounts'

urlpatterns = [
    path('account_list/', views.account_list),
    path('account/<int:pk>/', views.account),
    path('login/', views.login),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('get/',views.get, name = 'get'),
    # path('post/',views.post, name = 'post'),
]