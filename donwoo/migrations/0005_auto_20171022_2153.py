# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import donwoo.sku_models


class Migration(migrations.Migration):

    dependencies = [
        ('donwoo', '0004_skufile_filetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skufile',
            name='file',
            field=models.FileField(upload_to=donwoo.sku_models.sku_upload_to),
        ),
    ]
