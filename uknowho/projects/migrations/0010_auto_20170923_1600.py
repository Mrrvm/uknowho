# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-23 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20170923_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]