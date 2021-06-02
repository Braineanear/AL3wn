from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

Bassem_TYPES = (
	('1', '1'),
	('2', '2'),
	('3', '3'),
	('up', 'up'),
	('perfect', 'perfect'),
	('read', 'read'),
	('bank', 'bank'),
	('innovate','innovate')
	)

PUBLISHERS = (
	('EE', 'Mr. Ehab El Shafey'),
	('EA', 'Mr. Anis Fawzy'),
	('EG', 'Mr. Ehab Gaber'),
	('GA', 'Herr Ali Rashed'),
	('GM', 'Herr Mohammed Abdel Atty'),
	('AH', 'Mohammed Abdel Halem'),
	('GS', 'Herr Shady'),
	("GK", "Herr Khaled Bakheet")
	)

WRITERS = (
	('AMS', 'AMS'),
	('AA', 'Ashraf'),
	('HA', 'Hala'),
	('MM', 'Maryam'),
	('MG', 'Gouda'),
	('A2', '2001')
	)

SCHOOL_YEAR = (
	('1', '1'),
	('2', '2'),
	('3', '3'),
	('3Open', '3open')

	)

BASSEM_MAIN_SORT = (
	('maintab1', '1'),
	('maintab2', '2'),
	('maintab3', '3'),
	('maintab4', 'النحو'),
	('maintab5', 'البلاغة'),
	('maintab6', 'المتحرر'),
	('maintab7', 'ارتق'),
	('maintab8', 'دقيقتين'),
	('maintab9', 'تكات'),
	('maintab10', 'تحفيزي')
	)

BASSEM_SORT2 =(
	('subtab1', 'النحو'),
	('subtab2', 'البلاغة'),
	('subtab3', 'المتحرر'),
	('subtab4', 'أدب'),
	('subtab5', 'منوعات'),
	('subtab6', 'تحفيزي'),
	('subtab7', 'دقيقتين'),
	('subtab8', 'تكات'),
	('subtab9', 'ارتق'),
	('subtab10', 'اعراب'),
	('subtab11', 'دروس بلاغة')
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
	video_id = models.CharField(max_length=512)
	main_sort = models.CharField(choices=BASSEM_MAIN_SORT, max_length=255)
	sort2 = models.CharField(choices=BASSEM_SORT2, max_length=255, blank=True, null=True)
	featured = models.BooleanField(default=False)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title


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
		return self.title
