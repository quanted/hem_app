# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 15:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hem_app', '0009_auto_20170308_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='runhistory',
            name='categories',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hem_app.Category'),
            preserve_default=False,
        ),
    ]
