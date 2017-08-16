# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 11:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programming_languages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('subjective', 'Subjective'), ('objective', 'Objective')], default='subjective', max_length=20)),
                ('question_text', models.TextField(max_length=1000)),
                ('subjective_answer', models.TextField(blank=True, max_length=4000, null=True)),
                ('answer_keywords', models.TextField(blank=True, max_length=500, null=True)),
                ('candidate_experienced', models.PositiveSmallIntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('added_by', models.CharField(blank=True, max_length=100)),
                ('added_on', models.DateTimeField(blank=True)),
                ('updated_by', models.CharField(blank=True, max_length=100, null=True)),
                ('updated_on', models.DateTimeField(blank=True, null=True)),
                ('deactivated_by', models.CharField(blank=True, max_length=100, null=True)),
                ('deactivated_on', models.DateTimeField(blank=True, null=True)),
                ('programming_language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='programming_languages.ProgrammingLanguage')),
            ],
            options={
                'db_table': 'questions',
            },
        ),
        migrations.CreateModel(
            name='QuestionChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_choice_text', models.CharField(max_length=500, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('added_by', models.CharField(blank=True, max_length=100)),
                ('added_on', models.DateTimeField(blank=True)),
                ('updated_by', models.CharField(blank=True, max_length=100, null=True)),
                ('updated_on', models.DateTimeField(blank=True, null=True)),
                ('deactivated_by', models.CharField(blank=True, max_length=100, null=True)),
                ('deactivated_on', models.DateTimeField(blank=True, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions_answers.Question')),
            ],
            options={
                'db_table': 'question_choices',
            },
        ),
    ]
