# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hdcrm', '0024_auto_20171011_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='hetong',
            field=models.FileField(blank=True, upload_to='contracts/hetong'),
        ),
    ]
