# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]