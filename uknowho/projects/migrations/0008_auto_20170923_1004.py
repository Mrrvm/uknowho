# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-23 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20170923_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='userid',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
