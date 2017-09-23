from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    phoneNumber = models.IntegerField()
    #email = models.CharField(max_length=50)
    linkedIn = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    photo = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('user:detail', kwargs={'pk': self.pk})

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




class Skill(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill = models.CharField(max_length=50)


class Language(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    language = models.CharField(max_length=40)
