from django.db import models

class HalemURL(models.Model):
	link = models.URLField(default='http://al3wn.com/', max_length=512)

	def __str__(self):
		return "Halem Zoom URL"

	def get_absolute_url(self):
		return self.link