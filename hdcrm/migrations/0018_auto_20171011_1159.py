# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hdcrm', '0017_skuitem_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
