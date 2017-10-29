# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 13:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hdcrm', '0033_auto_20171019_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherLatex',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hdcrm.Product')),
                ('color', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
            ],
            bases=('hdcrm.product',),
        ),
        migrations.CreateModel(
            name='OtherProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hdcrm.Product')),
                ('color', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
            ],
            bases=('hdcrm.product',),
        ),
        migrations.CreateModel(
            name='Pvc',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hdcrm.Product')),
                ('color', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('material', models.CharField(max_length=20)),
            ],
            bases=('hdcrm.product',),
        ),
    ]