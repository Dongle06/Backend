from django.db import models

class Storage(models.Model) :
    created = models.DateTimeField(auto_now_add=True)
    userId = models.IntegerField()
    page = models.CharField(max_length=50)

    class Meta :
        ordering = ('created',)

    # def __str__(self):
    #     return self.userId
