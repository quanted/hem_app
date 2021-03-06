# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 18:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    '''Auto Generated Migration Files'''
    dependencies = [
        ('hem_app', '0004_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chemical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtxrid', models.TextField(max_length=50)),
                ('title', models.TextField(max_length=255)),
                ('cas', models.TextField(max_length=75)),
                ('mw', models.DecimalField(decimal_places=4, max_digits=11)),
                ('vp_pa', models.DecimalField(decimal_places=10, max_digits=16)),
                ('log_kow', models.DecimalField(decimal_places=4, max_digits=11)),
                ('water_sol_mg_L', models.DecimalField(decimal_places=6, max_digits=16)),
                ('log_koa', models.DecimalField(decimal_places=4, max_digits=11)),
                ('hlc_pa_m3_mole', models.DecimalField(decimal_places=10, max_digits=16)),
                ('half_hy_hrs', models.IntegerField()),
                ('half_sediment_hr', models.IntegerField()),
                ('half_soil_hr', models.IntegerField()),
                ('half_water_hr', models.IntegerField()),
                ('half_air_hr', models.DecimalField(decimal_places=10, max_digits=16)),
                ('removal', models.DecimalField(decimal_places=4, max_digits=11)),
                ('kp', models.DecimalField(decimal_places=4, max_digits=11)),
            ],
            options={
                'ordering': ('title', 'dtxrid'),
            },
        ),
        migrations.CreateModel(
            name='Dose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('intake_ingest_mgkgBW_d', models.DecimalField(decimal_places=15, max_digits=16)),
                ('intake_derm_mgkgBW_d', models.DecimalField(decimal_places=15, max_digits=16)),
                ('intake_inhal_mgkgBW_d', models.DecimalField(decimal_places=15, max_digits=16)),
                ('peak_hourly_air_conc_ug_m3', models.DecimalField(decimal_places=15, max_digits=16)),
                ('peak_dermal_loading_ug', models.DecimalField(decimal_places=15, max_digits=16)),
                ('disposal_solid_waste_ug', models.DecimalField(decimal_places=15, max_digits=16)),
                ('disposal_window_ug', models.DecimalField(decimal_places=15, max_digits=16)),
                ('disposal_sanitary_drain_ug', models.DecimalField(decimal_places=15, max_digits=16)),
                ('disposal_outdoor_surface_ug', models.DecimalField(decimal_places=15, max_digits=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chemical', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hem_app.Chemical')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hem_app.Person')),
                ('run_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hem_app.RunParams')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AlterModelOptions(
            name='trait',
            options={'ordering': ('title',)},
        ),
    ]
