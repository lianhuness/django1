# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 03:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hdcrm', '0030_auto_20171018_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='latexband',
            name='round',
            field=models.CharField(choices=[('ZHIJIAO', '直角'), ('YUANJIAO', '圆角')], default='ZHIJIAO', max_length=10),
        ),
    ]
