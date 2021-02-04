from django.template import RequestContext
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.views.generic import ListView

from .models import OuterExam, HalemURL, HerrShadyURL, HerrAliURL, MrEhabURL, HerrMURL, BassemURL, BassemYouTubeURL, HerrKhaledURL

from users.models import Applicant

User = get_user_model()


def home(request):
	context = {'title' : _('Home')}
	return render (request, 'core/index.html', context)

def about(request):
	usernumb = User.objects.all().count() + Applicant.objects.all().count()
	courses = Group.objects.all().count()
	staff = User.objects.all().filter(is_staff=True).count()
	context = {'usernumb' : usernumb, 'courses': courses, 'staff':staff ,'title' : _('About Us')}
	return render (request, 'core/about.html', context)

def dev(request):
	return render (request, 'core/dev.html')

def price(request):
	context = {'title' : _('Pricing')}
	return render (request, 'core/price.html', context)

def dashboard(request):
	context = {'title' : _('Dashboard')}
	return render (request, 'core/dashboard.html', context)

def sec(request):
	context = {'title' : _('Secondary')}
	return render (request, 'core/secondary.html', context)

def youtube(request):
	response = HttpResponse('', status=302)
	# AL3wn youtube
	response['Location'] = 'https://m.youtube.com/channel/UCWAITmc04Vcv9eaKt94Ujyw?sub_confirmation=1'
	return response
'''
def not_found(request, exception):
	return HttpResponseNotFound(request, '404.html')
'''
def stage1(request):
	context = {'title' : _('Stage 1')}
	return render (request, 'core/stage1.html', context)

def stage2(request):
	context = {'title' : _('Stage 2')}
	return render (request, 'core/stage2.html', context)

# Deutsch Akademie
def herr_shady(request):
	link = HerrShadyURL.objects.all()[0].link
	context = {'title' : _('Herr Shady'), 'link': link}
	return render(request, 'deutsch_akademie/shady.html', context)

def shady_lesson(request):
	response = HttpResponse('', status=302)
	# Zoom Link
	response['Location'] = HerrShadyURL.objects.all()[0].link
	return response

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Herr Shady Sec.1').exists())
def first_shady(request):
	link = HerrShadyURL.objects.all()[0].link
	context = {'title' : _('First Grade'), 'link': link}
	return render(request, 'deutsch_akademie/first.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Herr Shady Sec.2').exists())
def second_shady(request):
	link = HerrShadyURL.objects.all()[0].link
	context = {'title' : _('Second Grade'), 'link': link}
	return render(request, 'deutsch_akademie/second.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Herr Shady Sec.3').exists())
def third_shady(request):
	link = HerrShadyURL.objects.all()[0].link
	context = {'title' : _('third Grade'), 'link': link}
	return render(request, 'deutsch_akademie/third.html', context)

# HerrAliRashed
def herr_ali(request):
	link = HerrAliURL.objects.all()[0].link
	context = {'title' : _('Herr Ali'), 'link': link}
	return render(request, 'AliRashed/ali.html', context)

@login_required
# @user_passes_test(lambda u: u.groups.filter(name='Herr Shady Sec.1').exists())
def first_ali(request):
	link = HerrAliURL.objects.all()[0].link
	context = {'title' : _('First Grade'), 'link': link}
	return render(request, 'AliRashed/first.html', context)

@login_required
# @user_passes_test(lambda u: u.groups.filter(name='Herr Shady Sec.2').exists())
def second_ali(request):
	link = HerrAliURL.objects.all()[0].link
	context = {'title' : _('Second Grade'), 'link': link}
	return render(request, 'AliRashed/second.html', context)

@login_required
# @user_passes_test(lambda u: u.groups.filter(name='Herr Shady Sec.3').exists())
def third_ali(request):
	link = HerrAliURL.objects.all()[0].link
	context = {'title' : _('third Grade'), 'link': link}
	return render(request, 'AliRashed/third.html', context)

# Herr Mohammed Abdel Atty
def herr_m(request):
	link = HerrMURL.objects.all()[0].link
	context = {'title' : _('Herr M. Abdel Atty'), 'link': link}
	return render(request, 'HerrAbdelAtty/M.html', context)

@login_required
# @user_passes_test(lambda u: u.groups.filter(name='Herr Shady Sec.1').exists())
def first_m(request):
	link = HerrMURL.objects.all()[0].link
	context = {'title' : _('First Grade'), 'link': link}
	return render(request, 'HerrAbdelAtty/first.html', context)

@login_required
# @user_passes_test(lambda u: u.groups.filter(name='Herr Shady Sec.2').exists())
def second_m(request):
	link = HerrMURL.objects.all()[0].link
	context = {'title' : _('Second Grade'), 'link': link}
	return render(request, 'HerrAbdelAtty/second.html', context)

@login_required
# @user_passes_test(lambda u: u.groups.filter(name='Herr Shady Sec.3').exists())
def third_m(request):
	link = HerrMURL.objects.all()[0].link
	context = {'title' : _('third Grade'), 'link': link}
	return render(request, 'HerrAbdelAtty/third.html', context)

# Herr Khaled Bakheet
def herr_bakheet(request):
	link = HerrKhaledURL.objects.all()[0].link
	context = {'title' : _('Herr Khaled Bakheet'), 'link': link}
	return render(request, 'bakheet/khaled.html', context)

@login_required
# @user_passes_test(lambda u: u.groups.filter(name='Herr Shady Sec.1').exists())
def first_bakheet(request):
	publisher = 'Herr Khaled Bakheet'
	link = HerrKhaledURL.objects.all()[0].link
	exams = OuterExam.objects.all().filter(year='1', publisher='GK').order_by('-date_posted')
	context = {'title' : _('First Grade'),'exams':exams, 'link': link, 'publisher': publisher}
	return render(request, 'dash/exam_lesson.html', context)

@login_required
# @user_passes_test(lambda u: u.groups.filter(name='Herr Shady Sec.2').exists())
def second_bakheet(request):
	publisher = 'Herr Khaled Bakheet'
	link = HerrKhaledURL.objects.all()[0].link
	exams = OuterExam.objects.all().filter(year='2', publisher='GK').order_by('-date_posted')
	context = {'title' : _('Second Grade'),'exams':exams, 'link': link, 'publisher': publisher}
	return render(request, 'dash/exam_lesson.html', context)

@login_required
# @user_passes_test(lambda u: u.groups.filter(name='Herr Shady Sec.3').exists())
def third_bakheet(request):
	publisher = 'Herr Khaled Bakheet'
	link = HerrKhaledURL.objects.all()[0].link
	exams = OuterExam.objects.all().filter(year='3', publisher='GK').order_by('-date_posted')
	context = {'title' : _('third Grade'),'exams':exams, 'link': link, 'publisher': publisher}
	return render(request, 'dash/exam_lesson.html', context)

# halem
@login_required
# @user_passes_test(lambda u: u.groups.filter(name='Herr Shady Sec.3').exists())
def third_halem(request):
	link = HalemURL.objects.all()[0].link
	context = {'title' : _('third Grade'), 'link': link}
	return render(request, 'halem/third.html', context)


@login_required
def halem_lesson(request):
	response = HttpResponse('', status=302)
	# Zoom Link
	response['Location'] = HalemURL.objects.all()[0].link
	return response

# bassem
class FirstBassem(LoginRequiredMixin, ListView):
	template_name = 'bassem/first.html'
	context_object_name = 'link'
	paginate_by = 6

	def get_queryset(self):
		return BassemURL.objects.all().filter(kind='1').order_by('-date_posted')

	def get_context_data(self, *args, **kwargs):
		context = super(FirstBassem, self).get_context_data(*args, **kwargs)
		context['title'] = "First Grade"
		return context

class SecondBassem(LoginRequiredMixin, ListView):
	template_name = 'bassem/second.html'
	context_object_name = 'link'
	paginate_by = 6

	def get_queryset(self):
		return BassemURL.objects.all().filter(kind='2').order_by('-date_posted')

	def get_context_data(self, *args, **kwargs):
		context = super(SecondBassem, self).get_context_data(*args, **kwargs)
		context['title'] = "Second Grade"
		return context

class ThirdBassem(LoginRequiredMixin, ListView):
	template_name = 'bassem/third.html'
	context_object_name = 'link'
	paginate_by = 6

	def get_queryset(self):
		return BassemURL.objects.all().filter(kind='3').order_by('-date_posted')

	def get_context_data(self, *args, **kwargs):
		context = super(ThirdBassem, self).get_context_data(*args, **kwargs)
		context['title'] = "Third Grade"
		return context

class UpBassem(ListView):
	template_name = 'bassem/up.html'
	context_object_name = 'link'
	paginate_by = 6

	def get_queryset(self):
		return BassemURL.objects.all().filter(kind='up').order_by('-date_posted')


	def get_context_data(self, *args, **kwargs):
		context = super(UpBassem, self).get_context_data(*args, **kwargs)
		context['title'] = "Up"
		return context

class PerfectBassem(ListView):
	template_name = 'bassem/perfect.html'
	context_object_name = 'link'
	paginate_by = 6

	def get_queryset(self):
		return BassemURL.objects.all().filter(kind='perfect').order_by('-date_posted')

	def get_context_data(self, *args, **kwargs):
		context = super(PerfectBassem, self).get_context_data(*args, **kwargs)
		context['title'] = "Perfect"
		return context

class InnovateBassem(ListView):
	template_name = 'bassem/perfect.html'
	context_object_name = 'link'
	paginate_by = 6

	def get_queryset(self):
		return BassemURL.objects.all().filter(kind='innovate').order_by('-date_posted')

	def get_context_data(self, *args, **kwargs):
		context = super(InnovateBassem, self).get_context_data(*args, **kwargs)
		context['title'] = "Innovate"
		return context

class VideosBassem(ListView):
	model = BassemYouTubeURL
	template_name = 'core/subjects.html'
	context_object_name = 'link'
	ordering = ['-date_posted']
	paginate_by = 6

	def get_context_data(self, *args, **kwargs):
		context = super(VideosBassem, self).get_context_data(*args, **kwargs)
		context['title'] = "Videos"
		return context


def bassem_youtube(request):
	response = HttpResponse('', status=302)
	# AL3wn youtube
	response['Location'] = 'https://m.youtube.com/channel/UCRElkYWugZwq5kgIFFfsTMg?sub_confirmation=1'
	return response

# Ehab El Shafey
def ehab_elshafey(request):
	link = MrEhabURL.objects.all()[0].link
	context = {'title' : _('Ehab El Shafey'), 'link': link}
	return render(request, 'ehab/ehab.html', context)

@login_required
# @user_passes_test(lambda u: u.groups.filter(name='Herr Shady Sec.2').exists())
def second_ehab(request):
	link = MrEhabURL.objects.all()[0].link
	context = {'title' : _('Second Grade'), 'link': link}
	return render(request, 'ehab/second.html', context)

@login_required
# @user_passes_test(lambda u: u.groups.filter(name='Herr Shady Sec.3').exists())
def third_ehab(request):
	link = MrEhabURL.objects.all()[0].link
	context = {'title' : _('third Grade'), 'link': link}
	return render(request, 'ehab/third.html', context)

def ehab_trans(request):
	response = HttpResponse('', status=302)
	# Zoom Link
	response['Location'] = 'https://docs.google.com/forms/d/e/1FAIpQLScHdyI0KbWSiRQRitDH8i3yrqqY5xyzgids3kaQgDNx1PUv7g/viewform?usp=sf_link'
	return response