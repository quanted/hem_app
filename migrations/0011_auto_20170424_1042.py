# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-24 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hem_app', '0010_auto_20170424_0922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neverever',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puc_id', models.TextField(default=b'', max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('puc_id',),
            },
        ),
        migrations.AlterField(
            model_name='chemical',
            name='hlc_pa_m3_mole',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
        migrations.AlterField(
            model_name='chemical',
            name='vp_pa',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
    ]
