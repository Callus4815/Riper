from django.db import models
from django.core.validators import URLValidator

# Create your models here.

class Fruit(models.Model):
	name = models.CharField(max_length=50)
	color = models.CharField(max_length=25)
	type = models.CharField(max_length=25)
	description = models.CharField(max_length=255)
	url = models.CharField(max_length=50, default="none", validators=[URLValidator()])


	def __str__(self):
		return "{}<>{}<>{}".format(self.name, self.color, self.description)