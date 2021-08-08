from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from reserve.models import Applicant, Teacher, Class, Year
from reserve.views import StaffRequiredMixin

User = get_user_model()

class TeacherView(DetailView):
	template_name = 'report/teacher.html'
	model = Teacher
	# context_object_name = 'teacher'

	def get_queryset(self):
		return super().get_queryset().filter(slug=self.kwargs['slug'])

	def get_context_data(self, *args, **kwargs):
		context = super(TeacherView, self).get_context_data(*args, **kwargs)
		context['title'] = self.kwargs['slug']
		return context


class StudentListView(StaffRequiredMixin, ListView):
	template_name = 'report/view.html'
	context_object_name = 'students'
	paginate_by = 100

	def get_queryset(self, **kwargs):
		return Group.objects.get(name="Anis Sec.3").user_set.all()

	def get_context_data(self, *args, **kwargs):
		context = super(StudentListView, self).get_context_data(*args, **kwargs)
		context['title'] = self.kwargs['teacher']

		return context