# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-01 14:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hem_app', '0017_auto_20170427_0742'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chemical',
            options={'ordering': ('title', 'dtxsid')},
        ),
        migrations.RenameField(
            model_name='chemical',
            old_name='dtxrid',
            new_name='dtxsid',
        ),
    ]
