# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-21 20:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20170908_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectiondefault',
            name='image',
        ),
    ]
