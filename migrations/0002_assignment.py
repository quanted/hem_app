# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    '''Auto Generated Migration Files'''
    dependencies = [
        ('hem_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_title', models.TextField(max_length=2)),
                ('title', models.TextField(max_length=75)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
