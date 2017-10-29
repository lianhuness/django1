# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkuGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkuImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='donwoo/sku/')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donwoo.Sku')),
            ],
        ),
        migrations.CreateModel(
            name='SkuSupplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donwoo.Sku')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='skusupplier',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donwoo.Supplier'),
        ),
        migrations.AddField(
            model_name='sku',
            name='skuGroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donwoo.SkuGroup'),
        ),
    ]
