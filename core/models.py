from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

Bassem_TYPES = (
	('1', '1'),
	('2', '2'),
	('3', '3'),
	('up', 'up'),
	('perfect', 'perfect')
	)

PUBLISHERS = (
	('EE', 'Mr. Ehab El Shafey'),
	('GA', 'Herr Ali Rashed'),
	('GM', 'Herr Mohammed Abdel Atty'),
	('AH', 'Mohammed Abdel Halem'),
	('GS', 'Herr Shady')
	)

WRITERS = (
	('AMS', 'AMS'),
	('AA', 'Ashraf'),
	('HA', 'Hala'),
	('MM', 'Maryam'),
	('MG', 'Gouda')
	)

SCHOOL_YEAR = (
	('1', '1'),
	('2', '2'),
	('3', '3')
	)

class OuterExam(models.Model):
	title = models.CharField(max_length=255)
	writer = models.CharField(_('Writer'), choices=WRITERS, max_length=255)
	publisher = models.CharField(_('Publisher'), choices=PUBLISHERS, max_length=255)
	year = models.CharField(_('Academic Year'), choices=SCHOOL_YEAR, max_length=255)
	link = models.URLField(max_length=512)
	exam_day = models.DateField(blank=True, null=True)
	minutes_of_exam = models.IntegerField(blank=True, null=True)
	date_posted = models.DateTimeField(default=timezone.now)
	done = models.BooleanField(default=False)

	def __str__(self):
		return self.title

class HalemURL(models.Model):
	link = models.URLField(default='http://al3wn.com/', max_length=512)

	def __str__(self):
		return "Halem URL"

class BassemURL(models.Model):
	title = models.CharField(max_length=255)
	kind = models.CharField(_('Kind'), choices=Bassem_TYPES, max_length=255)
	link = models.URLField(default='http://al3wn.com/', max_length=512)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title


class BassemYouTubeURL(models.Model):
	title = models.CharField(max_length=255)
	link = models.URLField(default='http://al3wn.com/', max_length=512)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return "Bassem Youtube URL"


class HerrShadyURL(models.Model):
	title = models.CharField(max_length=255)
	link = models.URLField(default='http://al3wn.com/', max_length=512)

	def __str__(self):
		return "Herr Shady URL"


class HerrAliURL(models.Model):
	title = models.CharField(max_length=255)
	link = models.URLField(default='http://al3wn.com/', max_length=512)

	def __str__(self):
		return "Herr Ali URL"


class HerrMURL(models.Model):
	title = models.CharField(max_length=255)
	link = models.URLField(default='http://al3wn.com/', max_length=512)

	def __str__(self):
		return "Herr Mohammed Abdel Atty URL"

class HerrKhaledURL(models.Model):
	title = models.CharField(max_length=255)
	link = models.URLField(default='http://al3wn.com/', max_length=512)

	def __str__(self):
		return "Herr Khaled URL"

class MrEhabURL(models.Model):
	title = models.CharField(max_length=255)
	link = models.URLField(default='http://al3wn.com/', max_length=512)

	def __str__(self):
		return "Mr Ehab URL"
