from django import forms
from django.contrib.auth import get_user_model

from django.utils.translation import ugettext_lazy as _

from .models import Year, Teacher, Class, Applicant



class ApplicantForm(forms.ModelForm):
	phone_number = forms.FloatField(label=_('Phone Number'),
	max_value=1599999999, min_value=101111111)
	# classe = forms.ModelChoiceField(Class.objects.none(), widget=forms.RadioSelect)

	class Meta:
		model = Applicant
		fields = ['name', 'gender', 'email','address' ,'phone_number', 'a_phone_number',
		'school_type', 'classe']



class FilterForm(forms.Form):
	SUBJECT_CHOICE = (
	("Arabic",_("Arabic")),
	("English",_("English")),
	("biology",_("biology")),
	("Geology",_("Geology")),
	("Maths",_("Maths")),
	("science",_("science")),
	("Deutsch",_("Deutsch")),
	("French",_("French")),
	('Italian', _('Italian')),
	('Statistics', _('Statistics')),
	('Physics', _('Physics')),
	('Chemistry', _('Chemistry')),
	('philosophy', _('philosophy')),
	('psychology', _('psychology')),
	('Geography', _('Geography')),
	('history', _('history')),
	('Chinese', _('Chinese')),
	('Spanish', _('Spanish')),
	('Studies', _('Studies')),
	('None', 'None'),
	)

	subject = forms.ChoiceField(label=_('Subject'), choices=SUBJECT_CHOICE)