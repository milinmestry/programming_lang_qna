# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programming_lang', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('icno_url', models.URLField()),
                ('is_active', models.BooleanField()),
                ('added_by', models.CharField(max_length=100)),
                ('added_on', models.DateTimeField()),
                ('updated_by', models.CharField(max_length=100)),
                ('updated_on', models.DateTimeField()),
                ('deactivated_by', models.CharField(max_length=100)),
                ('deactivated_on', models.DateTimeField()),
            ],
        ),
    ]
