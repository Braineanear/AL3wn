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


MONTHS = (
	('1', _('January')),
	('2', _('February')),
	('3', _('March')),
	('4', _('April')),
	('5', _('May')),
	('6', _('June')),
	('7', _('July')),
	('8', _('August')),
	('9', _('September')),
	('10', _('October')),
	('11', _('November')),
	('12', _('December'))
	)

class Day(models.Model):
	day = models.CharField(max_length=9)

	def __str__(self):
		return self.day


class WorkDay(models.Model):
	date = models.DateField()

	def __str__(self):
		date = str(self.date)
		return date


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

'''
class Exam(models.Model):
	name = models.CharField(max_length=255)
	full_mark = models.FloatField()
	timestamp = models.DateTimeField(auto_now_add=True)
	at = models.DateField()
	teacher = models.ForeignKey(Teacher ,related_name='teacher' , on_delete=models.CASCADE)
	year = models.ForeignKey(Year, related_name='year', on_delete=models.CASCADE)
	semster = models.CharField(choices=SCHOOL_YEAR, max_length=255)

	def __str__(self):
		return self.name


class Grade(models.Model):
	value = models.FloatField()
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.student.username} on {self.exam}'

	def passed(self):
		pass

	def percent(self):
		pass


class Attendance(models.Model):
	classa = models.ForeignKey(Class, on_delete=models.CASCADE)
	student = models.ForeignKey(User, on_delete=models.CASCADE)

'''

class Fee(models.Model):
	value = models.FloatField()
	timestamp = models.DateTimeField(auto_now_add=True)
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	classa = models.ForeignKey(Class, on_delete=models.CASCADE)
	month = models.CharField(choices=MONTHS, max_length=2)
	is_paid = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.student.username} for {self.classa.teacher} in {self.month}'


# TODO
'''
when student enters a class all of his data is being made
check the data is unique
when student change class, his grades stic with him
'''