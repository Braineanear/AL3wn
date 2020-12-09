from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import Profile, Applicant

User = get_user_model()


class UserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name','email', 'region', 'year', 'phone_number', 'date_of_birth', 'gender', 'national_id', 'password1', 'password2')
        }),
        (_('Permissions'), {
            'fields': ('is_superuser', 'is_staff', 'is_student', 'is_publisher')
        })
    )
    fieldsets = (
        (_("Info"), {
            'fields': ('username', 'first_name', 'last_name','email', 'region', 'year', 'phone_number', 'gender', 'national_id', 'password')
        }),
        (_('Dates'), {
            'fields': ('date_of_birth' , 'date_joined', 'last_login')
        }),
        (_('Permissions'), {
            'fields': ('is_superuser', 'is_staff', 'is_student', 'is_publisher')
        })

    )
    list_display = ['username', 'first_name', 'phone_number', 'year', 'national_id']
    search_fields = ('username','first_name', 'last_name','national_id', 'phone_number',)
    ordering = ('username',)
    list_filter = ('gender', 'year', 'region',)


class ProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'image', 'image_tag']
    readonly_fields = ['image_tag']


class ApplicantAdmin(admin.ModelAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('full_name', 'personal_image', 'date_of_birth',
        'address', 'phone_number','a_phone_number', 'email',
        'national_id', 'available', 'college', 'year', 'gender',
        'why', 'how', 'what' ,'position')
        })
    )
    fieldsets = (
        (_('Pic'), {
            'fields': ('personal_image', 'image_tag')
        }),
        (_("Info"), {
            'fields': ('full_name','address',
        'phone_number','a_phone_number', 'email',
        'national_id', 'available', 'college', 'year', 'gender',
        'why', 'how', 'what' ,'position')
        }),
        (_('Dates'), {
            'fields': ('date_of_birth' , 'timestamp')
        })

    )

    readonly_fields = ['image_tag', 'timestamp']
    list_display = ['full_name', 'phone_number', 'year', 'national_id']
    search_fields = ('full_name','national_id','phone_number','a_phone_number', 'email',)
    ordering = ('full_name',)
    list_filter = ('gender', 'position', 'available', 'year', 'college',)


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Applicant, ApplicantAdmin)