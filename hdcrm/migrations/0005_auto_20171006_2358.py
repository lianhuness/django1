# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hdcrm', '0004_auto_20171006_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]