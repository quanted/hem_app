# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 15:40
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    """ auto generated RunHistory """
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RunHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.BooleanField(default=True)),
                ('gender', models.CharField(default=b'B', max_length=1)),
                ('population_size', models.PositiveIntegerField(default=10000)),
                ('min_age', models.PositiveSmallIntegerField(default=0)),
                ('max_age', models.PositiveSmallIntegerField(default=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
