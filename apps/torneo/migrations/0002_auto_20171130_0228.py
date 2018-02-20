# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-30 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torneo',
            name='sexo',
            field=models.CharField(choices=[('MAS', 'Masculino'), ('FEM', 'Femenino'), ('MIX', 'Mixto')], max_length=3),
        ),
    ]