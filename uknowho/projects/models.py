from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

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

    def __str__(self):
        return self.firstName + ' ' + self.lastName + '/' + self.username

    #def get_absolute_url(self):
    #    return reverse('user:detail', kwargs={'pk': self.pk})

# Create a profile first.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    photo = models.CharField(max_length=2000)
    duration = models.CharField(max_length=100)
    size = models.CharField(max_length=100)

    Other='ot'
    Software='sw'
    Hardware='hw'
    Music='ms'
    Art='ar'
    Sport='sp'
    projectType_CHOICES = ((Software,'software'),(Hardware, 'hardware'),(Music,'music'),(Art,'art'),(Sport,'sport'),(Other,'other'))

    projectType = models.CharField(max_length=2, choices=projectType_CHOICES, default=Other)

    #postdate = models.DateField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = None)

    def __str__(self):
        return self.title + ' ' + self.duration

    #return after form to. p.e. detail of project
    def get_absolute_url(self):
        return reverse('projects:index')

class Labels(models.Model):
    project=models.ForeignKey(Project, on_delete=models.CASCADE,default=None)
    label = models.CharField(max_length=30)#review


class Skill(models.Model):
    userid = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill = models.CharField(max_length=50)


class Language(models.Model):
    userid = models.ForeignKey(Profile, on_delete=models.CASCADE)
    language = models.CharField(max_length=40)


class Colaborators(models.Model):
    userid = models.ForeignKey(Profile, on_delete=models.CASCADE, default = None)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default = None)
