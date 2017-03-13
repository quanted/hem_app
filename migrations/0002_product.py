# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    # auto generated Product
    dependencies = [
        ('hem_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puc_id', models.TextField(editable=False)),
                ('category', models.TextField(max_length=75)),
                ('product_type', models.TextField(max_length=75)),
                ('product_type_refined', models.TextField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
