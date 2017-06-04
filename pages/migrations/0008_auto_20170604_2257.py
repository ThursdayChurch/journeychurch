# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
        ('pages', '0007_auto_20170529_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionVideo',
            fields=[
                ('content_ptr', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Content')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Video')),
            ],
            options={
                'verbose_name_plural': 'Sections - Video',
            },
            bases=('pages.content',),
        ),
        migrations.CreateModel(
            name='SectionVideoGroup',
            fields=[
                ('content_ptr', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Content')),
                ('video_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.VideoGroup')),
            ],
            options={
                'verbose_name_plural': 'Sections - Video Group',
            },
            bases=('pages.content',),
        ),
        migrations.AlterModelOptions(
            name='navigationitem',
            options={'verbose_name_plural': 'Navigation - Items'},
        ),
        migrations.AlterModelOptions(
            name='navigationmenu',
            options={'verbose_name_plural': 'Navigation - Menus'},
        ),
        migrations.AlterModelOptions(
            name='sectiondefault',
            options={'verbose_name_plural': 'Sections - Default Template'},
        ),
        migrations.AlterModelOptions(
            name='sectionthreecolumn',
            options={'verbose_name_plural': 'Sections - Three Column Template'},
        ),
        migrations.AlterModelOptions(
            name='sectiontwocolumn',
            options={'verbose_name_plural': 'Sections - Two Column Template'},
        ),
    ]
