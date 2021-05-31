from django.contrib import admin
from .models import Year, Teacher, Class, Applicant
from django.utils.translation import ugettext_lazy as _


class ApplicantAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Info"), {
            'fields': ('name','address', 'email','gender', 'school_type', 'timestamp',)
        }),
        (_('Number'), {
            'fields': ('phone_number','a_phone_number', 'uuid', 'passcode', 'classe')
        })
    )

    readonly_fields = ['timestamp']
    list_display = ['name','phone_number', 'uuid','school_type']
    search_fields = ('name','phone_number','a_phone_number', 'email', 'uuid',)
    ordering = ('timestamp',)
    list_filter = ('gender','school_type','classe__is_online', 'classe__year',
     'classe__teacher','classe__teacher__subject',)

admin.site.register(Year)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Applicant, ApplicantAdmin)
