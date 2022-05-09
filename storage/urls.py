from django.urls import path
from storage import views

app_name = 'storage'

urlpatterns = [
    path('storage_list', views.storage_list),
]
