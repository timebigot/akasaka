# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 20:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20160428_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='is_lunch',
        ),
    ]
