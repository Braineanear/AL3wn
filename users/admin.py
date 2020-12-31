from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import GroupAdmin as originalGroupAdmin


from .models import Profile, Applicant

User = get_user_model()


class UserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name','email', 'region', 'year', 'phone_number', 'date_of_birth', 'gender', 'national_id', 'password1', 'password2')
        }),
        (_('Permissions'), {
            'fields': ('groups', 'is_superuser', 'is_staff', 'is_student', 'is_publisher')
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
            'fields': ('groups', 'is_superuser', 'is_staff', 'is_student', 'is_publisher')
        })

    )
    list_display = ['username', 'first_name', 'phone_number', 'year', 'national_id']
    search_fields = ('username','first_name', 'last_name','national_id', 'phone_number',)
    ordering = ('username',)
    list_filter = ('gender', 'year','groups', 'region',)


class ProfileAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ['user', 'thumb']
    fields = ['user', 'image', 'image_tag']
    readonly_fields = ['image_tag']


class GroupAdminForm(forms.ModelForm):
    """
    ModelForm that adds an additional multiple select field for managing
    the users in the group.
    """
    users = forms.ModelMultipleChoiceField(
        User.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple('Users', False),
        required=False,
        )


    def __init__(self, *args, **kwargs):
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            initial_users = self.instance.user_set.values_list('pk', flat=True)
            self.initial['users'] = initial_users


    def save(self, *args, **kwargs):
        kwargs['commit'] = True
        return super(GroupAdminForm, self).save(*args, **kwargs)


    def save_m2m(self):
        self.instance.user_set.clear()
        self.instance.user_set.add(*self.cleaned_data['users'])


class GroupAdmin(originalGroupAdmin):
    """
    Customized GroupAdmin class that uses the customized form to allow
    management of users within a group.
    """
    form = GroupAdminForm
    list_display = ["name", "pk"]


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
        }),
        (_('Interview'), {
            'fields': ('notes1', 'rating1', 'notes2', 'rating2', 'accepted')
        })

    )

    readonly_fields = ['image_tag', 'timestamp']
    list_per_page = 40
    list_display = ['thumb', 'full_name', 'year']
    search_fields = ('full_name','national_id','phone_number','a_phone_number', 'email',)
    ordering = ('timestamp',)
    list_filter = ('gender', 'position', 'available', 'year', 'address',)


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Applicant, ApplicantAdmin)

# Register the modified GroupAdmin with the admin site
admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)