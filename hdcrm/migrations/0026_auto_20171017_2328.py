# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hdcrm', '0025_contract_hetong'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='hetong',
            field=models.FileField(blank=True, null=True, upload_to='contracts/hetong'),
        ),
    ]
