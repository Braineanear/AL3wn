from django.contrib import admin
from .models import Year, Teacher, Class, Applicant
from django.utils.translation import ugettext_lazy as _

class YearAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']

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

class ClassAdmin(admin.ModelAdmin):
	fieldsets = (
        (_("Info"), {
            'fields': ('name','uuid','teacher', 'is_privte', 'is_online', 'girls_only')
        }),
        (_('Number'), {
            'fields': ('year', 'number','max_number', 'start_at', 'semster')
        }))
	list_display = ['name', 'uuid','remaining', 'has_place', 'is_privte', 'is_online', 'girls_only']
	search_fields = ('name','uuid','teacher',)
	ordering = ('start_at',)
	list_filter = ('year', 'teacher', 'semster')

class TeacherAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'subject', 'rating']
	list_filter = ('years', 'subject', 'address')
	ordering = ('-rating',)


admin.site.register(Year, YearAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Applicant, ApplicantAdmin)
