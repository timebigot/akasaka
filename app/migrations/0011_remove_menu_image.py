# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 20:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_menu_is_lunch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='image',
        ),
    ]
