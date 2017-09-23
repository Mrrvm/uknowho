# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 22:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20170922_2206'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborators',
            name='User',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
