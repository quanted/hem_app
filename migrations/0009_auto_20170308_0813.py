# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hem_app', '0008_auto_20170308_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]