# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 17:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hdcrm', '0009_auto_20171007_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caigou',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hdcrm.Product')),
                ('specs', models.CharField(max_length=100)),
                ('material', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=50)),
            ],
            bases=('hdcrm.product',),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('POWERBAND208', '208圈'), ('POWERBAND101', '101圈'), ('5060MINIBAND', '50/60cm小圈'), ('CAIGOU', '外购件')], max_length=100),
        ),
        migrations.AddField(
            model_name='caigou',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hdcrm.Supplier'),
        ),
    ]
