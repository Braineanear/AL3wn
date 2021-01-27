from django.contrib import admin

from .models import OuterExam, HalemURL, HerrShadyURL, HerrAliURL, MrEhabURL, HerrMURL, BassemURL, BassemYouTubeURL

admin.site.register(HalemURL)
admin.site.register(HerrMURL)
admin.site.register(BassemURL)
admin.site.register(BassemYouTubeURL)
admin.site.register(MrEhabURL)
admin.site.register(HerrAliURL)
admin.site.register(HerrShadyURL)

class OuterExamAdmin(admin.ModelAdmin):
    list_display = ['title', 'publisher', 'year', 'minutes_of_exam', 'exam_day', 'done']
    ordering = ('date_posted',)
    list_filter = ('publisher', 'writer', 'done',)

admin.site.register(OuterExam, OuterExamAdmin)
