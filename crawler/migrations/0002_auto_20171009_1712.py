# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='words',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]