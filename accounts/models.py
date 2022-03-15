from pyexpat import model
from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    # nickname = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    # profile = models.URLField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField()

    def __str__(self):
        return self.user_id

