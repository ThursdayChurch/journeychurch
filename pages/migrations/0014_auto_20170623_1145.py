# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-23 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20170623_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigationitem',
            name='url',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
