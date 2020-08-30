from django.shortcuts import render
from django.utils.translation import gettext as _


def home(request):
	context = {'title' : _('Home')}
	return render (request, 'core/index.html', context)

def about(request):
	context = {'title' : _('About Us')}
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

def stage1(request):
	context = {'title' : _('Stage 1')}
	return render (request, 'core/stage1.html', context)

def stage2(request):
	context = {'title' : _('Stage 2')}
	return render (request, 'core/stage2.html', context)
