# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160428_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.FilePathField(path='/home/timebigot/Projects/akasaka/static/img/menu'),
        ),
    ]
