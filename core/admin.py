from django.contrib import admin

from .models import HalemURL, HerrShadyURL, HerrAliURL, MrEhabURL

admin.site.register(HalemURL)
admin.site.register(MrEhabURL)
admin.site.register(HerrAliURL)
admin.site.register(HerrShadyURL)
