# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 04:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('donwoo', '0007_skuquote'),
    ]

    operations = [
        migrations.AddField(
            model_name='skuquote',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
