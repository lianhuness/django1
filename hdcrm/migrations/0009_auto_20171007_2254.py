# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hdcrm', '0008_auto_20171007_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100, unique=True),
        ),
    ]