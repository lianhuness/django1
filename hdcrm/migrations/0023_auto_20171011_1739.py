# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hdcrm', '0022_auto_20171011_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='deliveryDate',
            field=models.DateField(auto_now=True),
        ),
    ]
