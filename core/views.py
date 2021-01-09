from django.template import RequestContext
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.utils.translation import gettext as _

from .models import HalemURL, HerrShadyURL, HerrAliURL, MrEhabURL, HerrMURL

from users.models import Applicant

User = get_user_model()


def home(request):
	context = {'title' : _('Home')}
	return render (request, 'core/index.html', context)

def about(request):
	usernumb = User.objects.all().count() + Applicant.objects.all().count()
	context = {'usernumb' : usernumb,'title' : _('About Us')}
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

# HerrAliRashed
def herr_m(request):
	link = HerrMURL.objects.all()[0].link
	context = {'title' : _('Herr M. Abdel Atty'), 'link': link}
	return render(request, 'HerrAbdelAtty/ali.html', context)

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


# halem
@login_required
# @user_passes_test(lambda u: u.groups.filter(name='Herr Shady Sec.3').exists())
def third_halem(request):
	context = {'title' : _('third Grade')}
	return render(request, 'halem/third.html', context)


@login_required
def halem_lesson(request):
	response = HttpResponse('', status=302)
	# Zoom Link
	response['Location'] = HalemURL.objects.all()[0].link
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