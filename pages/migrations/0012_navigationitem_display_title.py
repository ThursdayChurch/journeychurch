# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-23 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20170623_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigationitem',
            name='display_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]