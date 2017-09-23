from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Profile(models.Model):
    userid = models.CharField(default=' ', max_length=50)
    password = models.CharField(default=' ', max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    #email = models.CharField(max_length=50)
    linkedIn = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    photo = models.CharField(max_length=20)

    #def get_absolute_url(self):
    #    return reverse('user:detail', kwargs={'pk': self.pk})

class Labels(models.Model):
    label = models.CharField(max_length=30)#review

# Create a profile first.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    photo = models.CharField(max_length=2000)
    duration = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    projectType = models.IntegerField()
    #postdate = models.DateField()
    labels = Labels()
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, default = None)


class Skill(models.Model):
    userid = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill = models.CharField(max_length=50)


class Language(models.Model):
    userid = models.ForeignKey(Profile, on_delete=models.CASCADE)
    language = models.CharField(max_length=40)


class Colaborators(models.Model):
    userid = models.ForeignKey(Profile, on_delete=models.CASCADE, default = None)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default = None)

