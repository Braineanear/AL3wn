import os
from django.db import models
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

GENDER_CHOICE=(
	("Male","Male"),
	("Female","Female")
)

SCHOOL_YEAR = (
	('1', '1'),
	('2', '2'),
	('3', '3')
	)
POSITIONS_CHOICE = (
	('PR', "PR"),
	)

class User(AbstractUser):
	date_of_birth = models.DateField(_('date_of_birth'), blank=True, null=True)
	region = models.CharField(_('region'), blank=True, null=True, max_length=255)
	phone_number = models.FloatField(_('phone_number'))
	national_id = models.FloatField(_('national_id'), unique=True) 
	gender = models.CharField(_('gender'), choices=GENDER_CHOICE, max_length=255)
	year = models.CharField(_('year'), choices=SCHOOL_YEAR, max_length=255)
	is_student = models.BooleanField(_('is_student'), default=True)
	is_publisher = models.BooleanField(_('is_publisher'), default=False)

	def __str__(self):
		return self.username

	def image_verification(self):
		if self.profile.image == "default.jpg":
			return "No"
		else:
			return "Yes"

def get_upload_path(instance, filename):
    return os.path.join(
      'profile_pics', instance.user.gender, instance.user.username, filename)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to=get_upload_path)

	def __str__(self):
		return f'{self.user.username} Profile'

	def image_vertify(self):
		if self.image == "default.jpg":
			return "No"
		else:
			return "Yes"

	def image_tag(self):
		return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))

	def thumb(self):
		return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)


	image_tag.short_description = 'Image'


def personal_image_upload_path(instance, filename):
    return os.path.join(
      'applicant_pics', instance.gender, instance.full_name, filename)

class Applicant(models.Model):
	full_name = models.CharField(_('Full Name'), max_length=255)
	personal_image = models.ImageField(upload_to='applicant_pics')
	date_of_birth = models.DateField(_('Date of Birth'))
	address = models.CharField(_('Address'), max_length=512)
	phone_number = models.FloatField(_('Phone Number'))
	a_phone_number = models.FloatField(_('Phone Number (optional)'), blank=True, null=True)
	national_id = models.FloatField(_('National Id'), unique=True)
	available = models.BooleanField(_('Available for video interview'), default=False)
	college = models.CharField(_('College'), max_length=255)
	year = models.IntegerField(_('Academic Year'))
	gender = models.CharField(_('Gender'), choices=GENDER_CHOICE, max_length=255)
	why = models.TextField(_('Why Do you want to join us?'))
	how = models.TextField(_("How did you know about us"))
	what = models.TextField(_('What Skills do you have besides PR skills?'))
	position = models.CharField(_('Position'), choices=POSITIONS_CHOICE,
	 max_length=255, default='PR')
	timestamp = models.DateTimeField(auto_now_add=True)
	email = models.EmailField()
	# Interview Stuff
	notes1 = models.TextField(_('The first interviewer notes'), blank=True, null=True)
	rating1 = models.IntegerField(_('The first interviewer notes (/10)'), blank=True, null=True)
	notes2 = models.TextField(_('The second interviewer notes'), blank=True, null=True)
	rating2 = models.IntegerField(_('The second interviewer notes (/10)'), blank=True, null=True)
	accepted = models.BooleanField(_('Accepted'), default=False)


	def __str__(self):
		return self.full_name

	def image_tag(self):
		return mark_safe('<img src="%s" width="150" height="150" />' % (self.personal_image.url))

	def thumb(self):
		return mark_safe('<img src="%s" style="width: 20px; height:20px;" />' % self.personal_image.url)

	image_tag.short_description = 'Image'


	