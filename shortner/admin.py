from django.contrib import admin
from .models import Url

class UrlAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'views', 'link', 'user']

admin.site.register(Url, UrlAdmin)
