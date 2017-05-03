# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 15:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hem_app', '0019_auto_20170501_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='runhistory',
            name='chemical',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hem_app.Chemical'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='runparams',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hem_app.Category'),
            preserve_default=False,
        ),
    ]
