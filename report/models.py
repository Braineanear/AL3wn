from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from reserve.models import Teacher, Year

User = get_user_model()

SCHOOL_YEAR = (
	('1', '1'),
	('2', '2'),
	('3', '3')
	)


class Day(models.Model):
	day = models.CharField(max_length=9)

	def __str__(self):
		return self.day


class WorkDay(models.Model):
	date = models.DateField()

	def __str__(self):
		return self.date


class Class(models.Model):
	name = models.CharField(max_length=255)
	uuid = models.CharField(max_length=10)
	start_at = models.DateField()
	end_at = models.DateField(blank=True, null=True)
	days = models.ManyToManyField(Day)
	time = models.TimeField()
	duration = models.DurationField()
	work_days = models.ManyToManyField(WorkDay)
	teacher = models.ForeignKey(Teacher ,related_name='teacher' , on_delete=models.CASCADE)
	year = models.ForeignKey(Year, related_name='year', on_delete=models.CASCADE)
	is_private = models.BooleanField(default=False)
	is_online = models.BooleanField(default=False)
	girls_only = models.BooleanField(default=False)	
	semster = models.CharField(choices=SCHOOL_YEAR, max_length=255)
	students = models.ManyToManyField(User, related_name='student')

	def __str__(self):
		return self.name


	class Meta:
		verbose_name_plural = "classes"


# TODO
'''
class Grade
class attendance
class fee
'''