from django.contrib import admin
from .models import Year, Teacher, Class, Applicant

admin.site.register(Year)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Applicant)