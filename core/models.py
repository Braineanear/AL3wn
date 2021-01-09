from django.db import models

class HalemURL(models.Model):
	link = models.URLField(default='http://al3wn.com/', max_length=512)

	def __str__(self):
		return "Halem Zoom URL"


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
