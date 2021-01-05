from django.contrib import admin

from .models import HalemURL, HerrShadyURL, HerrAliURL

admin.site.register(HalemURL)
admin.site.register(HerrAliURL)
admin.site.register(HerrShadyURL)
