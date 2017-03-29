# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 19:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """ auto generated run history """

    dependencies = [
        ('hem_app', '0011_category_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run_id', models.IntegerField()),
                ('day', models.IntegerField()),
                ('activity', models.TextField(max_length=200)),
                ('start_time', models.DecimalField(decimal_places=2, max_digits=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='category',
            name='assignment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hem_app.ProductAssignment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hem_app.Category'),
        ),
    ]
