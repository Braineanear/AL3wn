from django.db import models

class Url(models.Model):
    link = models.URLField(max_length=512)
    uuid = models.CharField(max_length=10)
    views = models.IntegerField(default=0)
    user = models.BooleanField(default=False)

    def __str__(self):
		return self.uuid