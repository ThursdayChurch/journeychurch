# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('facebook', models.CharField(blank=True, max_length=2000)),
                ('twitter', models.CharField(blank=True, max_length=2000)),
                ('instagram', models.CharField(blank=True, max_length=2000)),
                ('youtube', models.CharField(blank=True, max_length=2000)),
                ('snapchat', models.CharField(blank=True, max_length=2000)),
            ],
        ),
    ]
