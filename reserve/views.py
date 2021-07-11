import os
import random

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.contrib.staticfiles import finders
from django.template.loader import get_template
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .models import Applicant, Teacher, Class, Year
from .forms import ApplicantForm, FilterForm


from xhtml2pdf import pisa
from excel_response import ExcelResponse


class Home(ListView):
	template_name = 'res/index.html'
	context_object_name = 'teachers'
	paginate_by = 8

	def get_queryset(self):
		return Teacher.objects.all().order_by('-rating')

	def get_context_data(self, *args, **kwargs):
		context = super(Home, self).get_context_data(*args, **kwargs)
		full = Applicant.objects.all().count()
		classes = Class.objects.all().count()
		Teachers = Teacher.objects.all().count()
		context['form'] = FilterForm
		context['title'] = "New Students"
		context['full'] = full
		context['classes'] = classes
		context['Teachers'] = Teachers
		return context

	def post(self, request):
		form = FilterForm(request.POST)
		if form.is_valid():
			answer = form.cleaned_data.get('subject')
			return redirect('ReserveSubject', subject=answer)


class SubjectFilter(ListView):
	template_name = 'res/index.html'
	context_object_name = 'teachers'
	paginate_by = 10

	def get_queryset(self, **kwargs):
		return Teacher.objects.all().filter(subject=self.kwargs['subject']).order_by('-rating')

	def get_context_data(self, *args, **kwargs):
		context = super(SubjectFilter, self).get_context_data(*args, **kwargs)
		full = Applicant.objects.all().count()
		classes = Class.objects.all().count()
		Teachers = Teacher.objects.all().count()
		context['form'] = FilterForm
		context['title'] = f"New Students {self.kwargs['subject']} Only"
		context['full'] = full
		context['classes'] = classes
		context['Teachers'] = Teachers
		return context

	def post(self, request, **kwargs):
		form = FilterForm(request.POST)
		if form.is_valid():
			answer = form.cleaned_data.get('subject')
			return redirect('ReserveSubject', subject=answer)


def All(request, teacher, year):
	if request.method == "POST":
		form = ApplicantForm(request.POST)
		if form.is_valid():
			applicant = form.save(commit=False)
			b = applicant.name
			try:
				Applicant.objects.get(name=b)
			except Applicant.DoesNotExist:
				if applicant.classe.has_place():
					numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
					passcode = ''.join(random.choice(numbers) for i in range(6))
					applicant.passcode = passcode
					d = applicant.classe.uuid
					s = applicant.classe.year.slug
					num = applicant.classe.number
					num = num+1
					dede = f'{d}{s}{num}'
					try:
						Applicant.objects.get(uuid=dede)
					except Applicant.DoesNotExist:
						applicant.uuid = dede
					else:
						num = num + 1
						dede = f'{d}{s}{num}'
						applicant.uuid = dede	

					pks = applicant.classe.pk
					clas = get_object_or_404(Class, pk=pks)
					clas.number = num
					clas.save()
					i = applicant.uuid
					form.save()
					messages.success(request, f'Your account has been Updated')
					return redirect(f'/new/report/{i}')
				else:
					messages.warning(request, f'This Class is Full. Try joining another Class!')
					return HttpResponseRedirect('#')
			else:
				messages.warning(request, f'You already have joined this Class!')
				haha = Applicant.objects.get(name=b)
				return redirect(f'/new/report/{haha.uuid}')
	else:
		form = ApplicantForm()
		form.fields['classe'].queryset = Class.objects.all().filter(teacher_id__slug=teacher,
		 year_id__slug=year)

	title = 'L.' + str(year) + ' ' + teacher
	context = {'form': form, 'title': title}
	return render (request, 'res/form.html', context)


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

	def test_func(self):
		return self.request.user.is_staff


class ApplicantListView(StaffRequiredMixin, ListView):
	template_name = 'res/view.html'
	context_object_name = 'students'
	paginate_by = 100

	def get_queryset(self, **kwargs):
		return Applicant.objects.all().filter(classe__teacher_id__slug=self.kwargs['teacher']).order_by('-timestamp')

	def get_context_data(self, *args, **kwargs):
		context = super(ApplicantListView, self).get_context_data(*args, **kwargs)
		full = Applicant.objects.all().filter(classe__teacher_id__slug=self.kwargs['teacher']).count()
		ys = Year.objects.all().filter(teacher__slug=self.kwargs['teacher'])
		for y in ys:
			context[f'L{y.slug}'] = y.name
			context[f'N{y.slug}'] = Applicant.objects.all().filter(classe__teacher_id__slug=self.kwargs['teacher'],
			classe__year__slug=y.slug).count()

		context['title'] = self.kwargs['teacher']
		context['full'] = full

		return context


class ClassListView(StaffRequiredMixin, ListView):
	template_name = 'res/view.html'
	context_object_name = 'students'
	paginate_by = 100

	def get_queryset(self, **kwargs):
		return Applicant.objects.all().filter(classe__teacher_id__slug=self.kwargs['teacher'],
		classe__uuid=self.kwargs['classe']).order_by('-timestamp')

	def get_context_data(self, *args, **kwargs):
		context = super(ClassListView, self).get_context_data(*args, **kwargs)
		full = Applicant.objects.all().filter(classe__teacher_id__slug=self.kwargs['teacher']).count()
		ys = Year.objects.all().filter(teacher__slug=self.kwargs['teacher'])
		for y in ys:
			context[f'L{y.slug}'] = y.name
			context[f'N{y.slug}'] = Applicant.objects.all().filter(classe__teacher_id__slug=self.kwargs['teacher'],
			classe__year__slug=y.slug).count()

		context['title'] = self.kwargs['teacher']
		context['full'] = full

		return context


def excelview(request, *args, **kwargs):
	objs = Applicant.objects.all().filter(classe__teacher_id__slug=kwargs.get('teacher')).order_by('-timestamp')
	return ExcelResponse(objs)


def applicant_render_pdf_view(request, *args, **kwargs):
	uuid = kwargs.get('uuid')
	student = get_object_or_404(Applicant, uuid=uuid)

	template_path = 'res/report.html'
	context = {'student': student}
	# Create a Django response object, and specify content_type as pdf
	response = HttpResponse(content_type='application/pdf')
	# if download
	# response['Content-Disposition'] = 'attachment; filename="report.pdf"'
	response['Content-Disposition'] = 'filename="report.pdf"'
	# find the template and render it.
	template = get_template(template_path)
	html = template.render(context)

	# create a pdf
	pisa_status = pisa.CreatePDF(html, dest=response)
	# if error then show some funy view
	if pisa_status.err:
		return HttpResponse('We had some errors <pre>' + html + '</pre>')
	return response

def render_pdf_view(request):
	template_path = 'res/report.html'
	context = {'myvar': "this is AM6's template context"}
	# Create a Django response object, and specify content_type as pdf
	response = HttpResponse(content_type='application/pdf')
	# if download
	# response['Content-Disposition'] = 'attachment; filename="report.pdf"'
	response['Content-Disposition'] = 'filename="report.pdf"'
	# find the template and render it.
	template = get_template(template_path)
	html = template.render(context)

	# create a pdf
	pisa_status = pisa.CreatePDF(html, dest=response)
	# if error then show some funy view
	if pisa_status.err:
		return HttpResponse('We had some errors <pre>' + html + '</pre>')
	return response