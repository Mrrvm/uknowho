from django.db import models

# Create your models here.

class User(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    phoneNumber = models.IntegerField()
    email = models.CharField(max_length=50)
    linkedIn = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    photo = models.CharField(max_length=20)


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=50)


class Language(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=40)
