from django.db import models

# Create your models here.
class PostModel(models.Model):
	title = models.CharField(max_length=50)
	content = models.CharField(max_length=50)
	author = models.CharField(max_length=30, blank=True)
	