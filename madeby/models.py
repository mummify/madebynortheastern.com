from django.db import models

class Creator(models.Model):
  first = models.CharField(max_length=200)
  last = models.CharField(max_length=200)
  grad_year = models.IntegerField(default=0)

class Project(models.Model):
  name = models.CharField(max_length=200)
  url = models.URLField(max_length=500)
  logo = models.ImageField(upload_to='logos')

  creators = models.ManyToManyField(Creator, related_name='projects')
