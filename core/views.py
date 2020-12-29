from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.utils.translation import gettext as _

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
	# return redirect('https://www.youtube.com/channel/UCWAITmc04Vcv9eaKt94Ujyw')
	res = HttpResponse('', status=302)
	res['Location'] = 'https://www.youtube.com/channel/UCWAITmc04Vcv9eaKt94Ujyw'
	return res

def stage1(request):
	context = {'title' : _('Stage 1')}
	return render (request, 'core/stage1.html', context)

def stage2(request):
	context = {'title' : _('Stage 2')}
	return render (request, 'core/stage2.html', context)

# Deutsch Akademie
@login_required
@user_passes_test(lambda u: u.groups.filter(name='Herr Shady Sec.1').exists())
def first_shady(request):
	context = {'title' : _('First Grade')}
	return render(request, 'deutsch_akademie/first.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Herr Shady Sec.2').exists())
def second_shady(request):
	context = {'title' : _('Second Grade')}
	return render(request, 'deutsch_akademie/second.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Herr Shady Sec.3').exists())
def third_shady(request):
	context = {'title' : _('third Grade')}
	return render(request, 'deutsch_akademie/third.html', context)