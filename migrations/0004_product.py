# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 12:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    '''Auto Generated Migration Files'''
    dependencies = [
        ('hem_app', '0003_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assignment', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hem_app.Assignment')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hem_app.Category')),
                ('traits', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hem_app.Trait')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]