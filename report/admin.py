from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Class, Day, WorkDay, Fee


class ClassAdmin(admin.ModelAdmin):
	fieldsets = (
        (_("Info"), {
            'fields': ('name','uuid','teacher', 'is_private', 'is_online', 'girls_only')
        }),
        (_('Number'), {
            'fields': ('year', 'days','time' , 'duration', 'start_at', 'end_at', 'semster')
        }),
        (_('Students'), {
            'fields': ('students', 'work_days')
        }))
	list_display = ['name', 'uuid', 'year']
	search_fields = ('name','uuid','teacher',)
	list_filter = ('year', 'teacher', 'semster', 'start_at')

class FeeAdmin(admin.ModelAdmin):
    list_filter = ['is_paid']

admin.site.register(Day)
admin.site.register(WorkDay)
admin.site.register(Fee, FeeAdmin)
admin.site.register(Class, ClassAdmin)
