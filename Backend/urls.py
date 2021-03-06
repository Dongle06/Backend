"""Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
# from django.conf.urls import url
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from rest_framework.permissions import AllowAny
# from rest_framework.permissions import routers, permissions

#swagger에서 api 문서로 보고싶은 url정의
schema_url_patterns = [
    path('api/', include('accounts.urls')) #밑에 있는 accounts.urls가는 url과 형식이 동일해야하나??
    ]

schema_view_v1 = get_schema_view(
    openapi.Info(
        title="Django API",
        default_version = 'v1',
        description = "dongle API 문서",
        terms_of_service = "https://www.google.com/policies/terms/",
        # contact = openapi.Contact(email="email"),
        license = openapi.License(name="")
    ),
    validators=['flex'],
    public = True,
    permission_classes = (AllowAny,),
    patterns = schema_url_patterns,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('users/', include('accounts.urls')),
    # path('accounts/', include('dj_rest_auth.urls')),
    # path('accounts/', include('dj_rest_auth.registration.urls')),
    # path('accounts/', include('allauth.urls')),
    path('api/', include('accounts.urls')), #나중에 accounts로 바꾸든지
    path('storage/', include('storage.urls')),
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'), 
    path(r'swagger', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), 
    path(r'redoc', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
