from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _


from .forms import UserResgiterForm

def register(request):
	if request.method == "POST":
		form = UserResgiterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get("username")
			messages.success(request, f'Acocunt created forn {username}')
			return redirect('/')
	else:
		form = UserResgiterForm()
	return render(request, 'users/register.html', {'form' : form, 'title' : _('Register')})