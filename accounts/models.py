# from django.utils.translation import ugettext_lazy as _


# class User(models.Model):
#     user_id = models.CharField(max_length=15)
#     password = models.CharField(max_length=20)
#     email = models.CharField(max_length=30)
#     # profile = models.URLField()
#     # created_at = models.DateTimeField(auto_now_add=True)
#     # updated_at = models.DateTimeField()

#     def __str__(self):
#         return self.user_id

# class User(AbstractUser) :
#     username = models.CharField(max_length=20, unique=True) #user_id
#     email = models.EmailField(max_length=50, unique=True)
#     user_id = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=20)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.user_id

from datetime import timezone
from pyexpat import model
from click import password_option
# from django.db import models

# class Account(models.Model):
#     username = models.CharField(max_length=40, unique = True)
#     email = models.CharField(max_length=200, unique = True)
#     password = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser) :
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=200, unique = True)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = []