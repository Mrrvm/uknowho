from django.db import models

# Create your models here.

class Labels(models.Model):
    label = models.CharField(max_length=30)

class Colaborators(models.Model):
    #User = models.ForeignKey(User, on_delete=models.CASCADE)
    pass
#class location(models.Model):

class Project(models.Model):
    title = models.CharField(max_length=100)
    miniDescription = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    photo = models.CharField(max_length=2000)
    duration = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    projectType = models.IntegerField()
    #postdate = models.DateField()
    colaborators = Colaborators()
    labels = Labels()
