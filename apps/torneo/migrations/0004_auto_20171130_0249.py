# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-30 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0003_torneo_deporte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torneo',
            name='nombre',
            field=models.CharField(blank=True, default='', max_length=70),
        ),
    ]
