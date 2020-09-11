from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

GENDER_CHOICE=(
	("Male",_("Male")),
	("Female",_("Female"))
)

SCHOOL_YEAR = (
	('1', '1'),
	('2', '2'),
	('3', '3')
	)

User = get_user_model()

class UserResgiterForm(UserCreationForm):
	region = forms.CharField(label=_('region'))
	date_of_birth = forms.DateField(label=_('date_of_birth'),
		 widget=forms.TextInput(attrs={'type': 'date'}))       
	phone_number = forms.FloatField(label=_('phone_number'),
	widget=forms.TextInput(attrs={'placeholder':'ex: 01553057088'}),
	max_value=1599999999, min_value=101111111)
	national_id = forms.FloatField(label=_('national_id'),
	widget=forms.TextInput(attrs={'placeholder':'ex: 30001011801881'}),
	max_value=99999999999999, min_value=10000000000000)
	gender = forms.ChoiceField(label=_('gender'), choices=GENDER_CHOICE)
	year = forms.ChoiceField(label=_('year'), choices=SCHOOL_YEAR)

	class Meta:
		model = User
		fields = ['username', 'region', 'phone_number', 'date_of_birth', 'gender', 'national_id', 'year', 'password1', 'password2']