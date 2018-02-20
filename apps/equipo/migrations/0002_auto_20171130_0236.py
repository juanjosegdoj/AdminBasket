# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-30 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='cestAfa',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='cestCon',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='cestDif',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='partGan',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='partJug',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='partPerd',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='partW',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='posicion',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='puntos',
            field=models.IntegerField(default=0),
        ),
    ]
