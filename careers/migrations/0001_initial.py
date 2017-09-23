# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-21 22:24
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, unique=True)),
                ('slug', models.SlugField(max_length=200, null=True, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('entry_date', models.DateTimeField(null=True)),
                ('expiration_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('open', 'Open'), ('closed', 'Closed')], default='open', max_length=6)),
                ('description', tinymce.models.HTMLField(blank=True, max_length=60000, null=True)),
                ('contact_name', models.CharField(max_length=100, null=True, unique=True)),
                ('contact_email', models.EmailField(max_length=254, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]