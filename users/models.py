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

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def image_tag(self):
		return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))

	image_tag.short_description = 'Image'