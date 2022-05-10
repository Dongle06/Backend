# # from xml.etree.ElementInclude import include
# from django.contrib.auth import views as auth_views
# # from rest_framework import routers

# # router = routers.DefaultRouter() #defaultRouter 설정
# # router.register('user', views.UserViewSet) #ViewSet과 함께 user라는 router 등록

# # urlpatterns = [
# #     path('', include(router.urls)),
# # ]

from django.urls import path
from accounts import views
from django.conf.urls import include

app_name = 'accounts'

urlpatterns = [
    path('account_list', views.account_list),
    path('signup', views.signup),
    path('account/<int:pk>', views.account),
    path('login', views.login),
    path('user/auth', views.authenticatedUser),
    path('logout', views.logout),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]