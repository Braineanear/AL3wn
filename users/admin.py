from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

# Removing Group
from django.contrib.auth.models import Group
admin.site.unregister(Group)

User = get_user_model()


class UserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('username', 'region', 'year', 'phone_number', 'date_of_birth', 'gender', 'national_id', 'password1', 'password2')
        }),
        (_('Permissions'), {
            'fields': ('is_superuser', 'is_staff', 'is_student', 'is_publisher')
        })
    )
    fieldsets = (
        (_("Info"), {
            'fields': ('username', 'region', 'year', 'phone_number', 'gender', 'national_id', 'password')
        }),
        (_('Dates'), {
            'fields': ('date_of_birth' , 'date_joined', 'last_login')
        }),
        (_('Permissions'), {
            'fields': ('is_superuser', 'is_staff', 'is_student', 'is_publisher')
        })

    )
    list_display = ['username', 'gender', 'year', 'is_student', 'is_publisher']
    search_fields = ('username',)
    ordering = ('username',)
    list_filter = ('gender', 'year', 'region',)


admin.site.register(User, UserAdmin)