# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-02-14 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0006_auto_20180214_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torneo',
            name='deporte',
            field=models.CharField(blank=True, default='Baloncesto', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='torneo',
            name='nombre',
            field=models.CharField(blank=True, default='', max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='torneo',
            name='sexo',
            field=models.CharField(choices=[('MAS', 'Masculino'), ('FEM', 'Femenino'), ('MIX', 'Mixto')], max_length=3, null=True),
        ),
    ]
