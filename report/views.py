from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.forms import modelformset_factory
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

from .models import Class, Fee
# from .forms import FeeUpdateForm

from reserve.models import Applicant, Teacher, Year
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
	context_object_name = 'class'

	def get_queryset(self, **kwargs):
		return Class.objects.all().filter(teacher_id__slug=self.kwargs['teacher'], year_id__slug=self.kwargs['year'])

	def get_context_data(self, *args, **kwargs):
		context = super(StudentListView, self).get_context_data(*args, **kwargs)
		context['title'] = self.kwargs['teacher']

		return context


@login_required
def StudentPage(request, *args, **kwargs):
	teach = kwargs.get('teacher')
	year = kwargs.get('year')
	classe = kwargs.get('classe')
	student = kwargs.get('student')
	FeeFormSet = modelformset_factory(Fee, fields=('is_paid',))
	if request.method == "POST":
		feeformset = FeeFormSet(
			request.POST, queryset=Fee.objects.all().filter(student__username=student, classa=classe).order_by('-month'),
			)
		if feeformset.is_valid():
			feeformset.save()
			messages.success(request, f'Your account has been Updated')
		my_queryset = Fee.objects.all().filter(student__username=student, classa=classe).order_by('month')
	else:
		my_queryset = Fee.objects.all().filter(student__username=student, classa=classe).order_by('month')

	namee = f'{teach} for {year} in {classe}: {student}'
	context = {
		'qs' : my_queryset,
		'title' : namee
	}
	return render(request, 'report/profile.html', context)


	'''
	if request.method == "POST":
		user_form = UserUpdateForm(request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, f'Your account has been Updated')
			return redirect('Student')
	else:
		# grades
		# Attendance
		# Fee
		user_form = UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)
	'''