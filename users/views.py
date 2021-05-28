from django.contrib import messages
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _

from .forms import UserResgiterForm, UserUpdateForm, ProfileUpdateForm, ApplicantForm

from core.views import AdminRequiredMixin

User = get_user_model()

def register(request):
	if request.user.is_authenticated:
		messages.success(request, f'You already have an Account!')
		return redirect('Profile')
	else:
		if request.method == "POST":
			form = UserResgiterForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data.get("username")
				messages.success(request, f'{username}, your account has been created! You can Log In')
				return redirect('Login')
		else:
			form = UserResgiterForm()
		return render(request, 'users/register.html', {'form' : form, 'title' : _('Register')})

	
@login_required
def profile(request):
	if request.method == "POST":
		user_form = UserUpdateForm(request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, f'Your account has been Updated')
			return redirect('Profile')
	else:
		user_form = UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)


	context = {
		'user_form': user_form,
		'profile_form': profile_form,
		'title' : request.user.username
	}
	return render(request, 'users/profile.html', context)

def career(request):
	if request.method == "POST":
		form = ApplicantForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f'Your data have been submitted😍! We will contact you💖')
			return redirect('Home')
	else:
		form = ApplicantForm()
	return render(request, 'users/career.html', {'form' : form, 'title' : _('Careers')})


class AllUsers(AdminRequiredMixin, ListView):
	template_name = 'core/birth.html'
	context_object_name = 'date'
	paginate_by = 12

	def get_queryset(self, **kwargs):
		return User.objects.all().filter(date_of_birth__year=str(self.kwargs['year']))

	def get_context_data(self, *args, **kwargs):
		context = super(AllUsers, self).get_context_data(*args, **kwargs)
		y = str(self.kwargs['year'])
		count = User.objects.all().filter(date_of_birth__year=str(self.kwargs['year'])).count()
		context['title'] = f"{y} Users"
		context['count'] = count
		return context