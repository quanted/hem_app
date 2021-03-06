# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-24 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hem_app', '0009_auto_20170418_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puc_id', models.TextField(default=b'', max_length=120)),
                ('variable_value', models.TextField(default=b'', max_length=25)),
                ('units', models.TextField(default=b'', max_length=25)),
                ('gender', models.CharField(max_length=1)),
                ('min_age', models.IntegerField(default=0)),
                ('max_age', models.IntegerField(default=99)),
                ('form_value', models.TextField(default=b'', max_length=25)),
                ('mean_value', models.DecimalField(decimal_places=7, max_digits=14)),
                ('cv_value', models.DecimalField(decimal_places=7, max_digits=14)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AlterField(
            model_name='person',
            name='ages',
            field=models.TextField(max_length=30),
        ),
    ]
