# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-06 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submittedforms',
            name='date',
            field=models.CharField(max_length=256, verbose_name='Date'),
        ),
    ]
