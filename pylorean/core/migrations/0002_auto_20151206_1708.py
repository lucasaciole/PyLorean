# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-06 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='busy_weekday',
            field=models.DateField(choices=[('2', 'Segunda-Feira'), ('3', 'Terça-Feira'), ('4', 'Quarta-Feira'), ('5', 'Quinta-Feira'), ('6', 'Sexta-Feira'), ('S', 'Sábado'), ('D', 'Domingo')]),
        ),
    ]
