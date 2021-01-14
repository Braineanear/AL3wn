from django.db import models
from django.utils import timezone

class HalemURL(models.Model):
	link = models.URLField(default='http://al3wn.com/', max_length=512)

	def __str__(self):
		return "Halem Zoom URL"

class Bassem01URL(models.Model):
	title = models.CharField(max_length=255)
	link = models.URLField(default='http://al3wn.com/', max_length=512)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return "Bassem 01 URL"

class Bassem02URL(models.Model):
	title = models.CharField(max_length=255)
	link = models.URLField(default='http://al3wn.com/', max_length=512)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return "Bassem 02 URL"

class Bassem03URL(models.Model):
	title = models.CharField(max_length=255)
	link = models.URLField(default='http://al3wn.com/', max_length=512)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return "Bassem 02 URL"

class BassemYouTubeURL(models.Model):
	title = models.CharField(max_length=255)
	link = models.URLField(default='http://al3wn.com/', max_length=512)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return "Bassem Youtube URL"

class BassemUpURL(models.Model):
	title = models.CharField(max_length=255)
	link = models.URLField(default='http://al3wn.com/', max_length=512)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return "Bassem Up URL"

class BassemPerfectURL(models.Model):
	title = models.CharField(max_length=255)
	link = models.URLField(default='http://al3wn.com/', max_length=512)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return "Bassem Perfect URL"

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


class MrEhabURL(models.Model):
	title = models.CharField(max_length=255)
	link = models.URLField(default='http://al3wn.com/', max_length=512)

	def __str__(self):
		return "Mr Ehab URL"
