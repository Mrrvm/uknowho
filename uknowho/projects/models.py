from django.db import models
from user.models import Profile

# Create your models here.

class Labels(models.Model):
    label = models.CharField(max_length=30)#review

class Colaborators(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default = None)

#class location(models.Model):

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    photo = models.CharField(max_length=2000)
    duration = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    projectType = models.IntegerField()
    #postdate = models.DateField()
    colaborators = Colaborators()
    labels = Labels()
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, default = None)
