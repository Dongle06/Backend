from django.contrib import admin

from storage.models import Storage

# Register your models here.
class StorageAdmin(admin.ModelAdmin) :
    list_display = ('userId', 'page', 'created',)

admin.site.register(Storage, StorageAdmin)