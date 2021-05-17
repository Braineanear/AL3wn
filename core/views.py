from datetime import datetime
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

	def test_func(self):
		return self.request.user.is_superuser

class Birthdays(AdminRequiredMixin, ListView):
	template_name = 'core/birth.html'
	context_object_name = 'date'
	paginate_by = 6

	def get_queryset(self):
		return User.objects.all().filter(date_of_birth__month=str(datetime.today().month), date_of_birth__day=str(datetime.today().day))

	def get_context_data(self, *args, **kwargs):
		context = super(Birthdays, self).get_context_data(*args, **kwargs)
		tday = datetime.today().date()
		context['title'] = "Birthdays"
		context['tday'] = tday
		return context


class AllBirthdays(AdminRequiredMixin, ListView):
	template_name = 'core/birth.html'
	context_object_name = 'date'
	paginate_by = 6

	def get_queryset(self, **kwargs):
		return User.objects.all().filter(date_of_birth__month=str(self.kwargs['month']), date_of_birth__day=str(self.kwargs['day']))

	def get_context_data(self, *args, **kwargs):
		context = super(AllBirthdays, self).get_context_data(*args, **kwargs)
		tday = datetime(year=2021, month=self.kwargs['month'], day=self.kwargs['day'])
		context['title'] = "Birthdays"
		context['tday'] = tday
		return context


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
@user_passes_test(lambda u: u.groups.filter(name='Herr Ali Sec.1').exists())
def first_ali(request):
	publisher = 'Herr Ali Rashed'
	link = HerrAliURL.objects.all()[0].link
	exams = OuterExam.objects.all().filter(year='1', publisher='GA').order_by('-date_posted')
	context = {'title' : _('First Grade'),'exams':exams, 'link': link, 'publisher': publisher}
	return render(request, 'dash/exam_lesson.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Herr Ali Sec.2').exists())
def second_ali(request):
	publisher = 'Herr Ali Rashed'
	link = HerrAliURL.objects.all()[0].link
	exams = OuterExam.objects.all().filter(year='2', publisher='GA').order_by('-date_posted')
	context = {'title' : _('Second Grade'),'exams':exams, 'link': link, 'publisher': publisher}
	return render(request, 'dash/exam_lesson.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Herr Ali Sec.3').exists())
def third_ali(request):
	publisher = 'Herr Ali Rashed'
	link = HerrAliURL.objects.all()[0].link
	exams = OuterExam.objects.all().filter(year='3', publisher='GA').order_by('-date_posted')
	context = {'title' : _('third Grade'),'exams':exams, 'link': link, 'publisher': publisher}
	return render(request, 'dash/exam_lesson.html', context)

# Herr Mohammed Abdel Atty
def herr_m(request):
	link = HerrMURL.objects.all()[0].link
	context = {'title' : _('Herr M. Abdel Atty'), 'link': link}
	return render(request, 'HerrAbdelAtty/M.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Herr M Sec.1').exists())
def first_m(request):
	link = HerrMURL.objects.all()[0].link
	context = {'title' : _('First Grade'), 'link': link}
	return render(request, 'HerrAbdelAtty/first.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Herr M Sec.2').exists())
def second_m(request):
	link = HerrMURL.objects.all()[0].link
	context = {'title' : _('Second Grade'), 'link': link}
	return render(request, 'HerrAbdelAtty/second.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Herr M Sec.3').exists())
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
@user_passes_test(lambda u: u.groups.filter(name='Herr Bakheet Sec.1').exists())
def first_bakheet(request):
	publisher = 'Herr Khaled Bakheet'
	link = HerrKhaledURL.objects.all()[0].link
	exams = OuterExam.objects.all().filter(year='1', publisher='GK').order_by('-date_posted')
	context = {'title' : _('First Grade'),'exams':exams, 'link': link, 'publisher': publisher}
	return render(request, 'dash/exam_lesson.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Herr Bakheet Sec.2').exists())
def second_bakheet(request):
	publisher = 'Herr Khaled Bakheet'
	link = HerrKhaledURL.objects.all()[0].link
	exams = OuterExam.objects.all().filter(year='2', publisher='GK').order_by('-date_posted')
	context = {'title' : _('Second Grade'),'exams':exams, 'link': link, 'publisher': publisher}
	return render(request, 'dash/exam_lesson.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Herr Bakheet Sec.3').exists())
def third_bakheet(request):
	publisher = 'Herr Khaled Bakheet'
	link = HerrKhaledURL.objects.all()[0].link
	exams = OuterExam.objects.all().filter(year='3', publisher='GK').order_by('-date_posted')
	context = {'title' : _('third Grade'),'exams':exams, 'link': link, 'publisher': publisher}
	return render(request, 'dash/exam_lesson.html', context)

# halem
@login_required
@user_passes_test(lambda u: u.groups.filter(name='Halem').exists())
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
class FirstBassem(LoginRequiredMixin, UserPassesTestMixin, ListView):
	template_name = 'bassem/first.html'
	context_object_name = 'link'
	paginate_by = 6

	def test_func(self):
		return self.request.user.groups.filter(name='Bassem Sec.1').exists()

	def get_queryset(self):
		return BassemURL.objects.all().filter(kind='1').order_by('-date_posted')

	def get_context_data(self, *args, **kwargs):
		context = super(FirstBassem, self).get_context_data(*args, **kwargs)
		context['title'] = "First Grade"
		return context

class SecondBassem(LoginRequiredMixin, UserPassesTestMixin, ListView):
	template_name = 'bassem/second.html'
	context_object_name = 'link'
	paginate_by = 6

	def test_func(self):
		return self.request.user.groups.filter(name='Bassem Sec.2').exists()

	def get_queryset(self):
		return BassemURL.objects.all().filter(kind='2').order_by('-date_posted')

	def get_context_data(self, *args, **kwargs):
		context = super(SecondBassem, self).get_context_data(*args, **kwargs)
		context['title'] = "Second Grade"
		return context

class ThirdBassem(LoginRequiredMixin, UserPassesTestMixin, ListView):
	template_name = 'bassem/third.html'
	context_object_name = 'link'
	paginate_by = 6

	def test_func(self):
		return self.request.user.groups.filter(name='Bassem Sec.3').exists()

	def get_queryset(self):
		return BassemURL.objects.all().filter(kind='3').order_by('-date_posted')

	def get_context_data(self, *args, **kwargs):
		context = super(ThirdBassem, self).get_context_data(*args, **kwargs)
		context['title'] = "Third Grade"
		return context

class UpBassem(ListView):
	template_name = 'bassem/perfect.html'
	context_object_name = 'link'
	paginate_by = 6

	def get_queryset(self):
		return BassemURL.objects.all().filter(kind='up').order_by('-date_posted')


	def get_context_data(self, *args, **kwargs):
		context = super(UpBassem, self).get_context_data(*args, **kwargs)
		context['title'] = "Up"
		context['ar_title'] = "ارتقٍ  "
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
		context['ar_title'] = "أتقن"
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
		context['ar_title'] = "أبدع"
		return context


class ReadBassem(ListView):
	template_name = 'bassem/perfect.html'
	context_object_name = 'link'
	paginate_by = 6

	def get_queryset(self):
		return BassemURL.objects.all().filter(kind='read').order_by('-date_posted')

	def get_context_data(self, *args, **kwargs):
		context = super(ReadBassem, self).get_context_data(*args, **kwargs)
		context['title'] = "Read"
		context['ar_title'] = "أقرأ"
		return context


class BankBassem(ListView):
	template_name = 'bassem/perfect.html'
	context_object_name = 'link'
	paginate_by = 6

	def get_queryset(self):
		return BassemURL.objects.all().filter(kind='bank').order_by('-date_posted')

	def get_context_data(self, *args, **kwargs):
		context = super(BankBassem, self).get_context_data(*args, **kwargs)
		context['title'] = "Bank"
		context['ar_title'] = "بَنْك الْمَعْرِفَة "
		return context


class VideosBassem(ListView):
	model = BassemYouTubeURL
	template_name = 'bassem/subjects.html'
	context_object_name = 'videos'
	ordering = ['-date_posted']
	paginate_by = 6

	def get_context_data(self, *args, **kwargs):
		context = super(VideosBassem, self).get_context_data(*args, **kwargs)
		context['title'] = "Videos"
		return context

class Firsts(ListView):
	template_name = 'core/firsts.html'
	context_object_name = 'date'

	def get_queryset(self):
		return User.objects.all().filter(groups__name__exact='test')

	def get_context_data(self, *args, **kwargs):
		context = super(Firsts, self).get_context_data(*args, **kwargs)
		context['title'] = "Firsts"
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
@user_passes_test(lambda u: u.groups.filter(name='Ehab Sec.2').exists())
def second_ehab(request):
	publisher = 'Mr. Ehab El Shafey'
	link = MrEhabURL.objects.all()[0].link
	exams = OuterExam.objects.all().filter(year='2', publisher='EE').order_by('-date_posted')
	context = {'title' : _('Second Grade'),'exams':exams, 'link': link, 'publisher': publisher}
	return render(request, 'dash/exam_lesson.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Ehab Sec.3').exists())
def third_ehab(request):
	publisher = 'Mr. Ehab El Shafey'
	link = MrEhabURL.objects.all()[0].link
	exams = OuterExam.objects.all().filter(year='3', publisher='EE').order_by('-date_posted')
	context = {'title' : _('third Grade'),'exams':exams, 'link': link, 'publisher': publisher}
	return render(request, 'dash/exam_lesson.html', context)

@login_required
def third_ehab_open(request):
	publisher = 'Mr. Ehab El Shafey'
	link = OuterExam.objects.all().filter(year='3Open', publisher='EE').order_by('-date_posted')
	context = {'title' : _('third Grade'),'link':link , 'publisher': publisher}
	return render(request, 'bassem/perfect.html', context)

# Ehab Gaber

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Ehab Gaber Sec.3').exists())
def third_ehab_gaber(request):
	publisher = 'Mr. Ehab Gaber'
	link = MrEhabURL.objects.all().filter(title='Mr. Ehab Gaber')[0].link
	exams = OuterExam.objects.all().filter(year='3', publisher='EG').order_by('-date_posted')
	context = {'title' : _('third Grade'),'exams':exams, 'link': link, 'publisher': publisher}
	return render(request, 'dash/exam_lesson.html', context)