# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 16:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hdcrm', '0029_contractexpense'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatexBand',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hdcrm.Product')),
                ('len', models.DecimalField(decimal_places=2, default=150, max_digits=10)),
                ('width', models.DecimalField(decimal_places=2, default=15, max_digits=10)),
                ('thickness', models.DecimalField(decimal_places=2, max_digits=10)),
                ('phantom', models.CharField(max_length=20)),
                ('color', models.CharField(choices=[('RED', '红'), ('ORANGE', '橙'), ('YELLOW', '黄'), ('GREEN', '绿'), ('BLUE', '蓝'), ('BLACK', '黑'), ('PURPLE', '紫'), ('PINK', '粉'), ('NOCOLOR', '本色')], max_length=20)),
            ],
            bases=('hdcrm.product',),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('POWERBAND208', '208圈'), ('POWERBAND101', '101圈'), ('5060MINIBAND', '50/60cm小圈'), ('CAIGOU', '外购件'), ('LATEXBAND', '乳胶片')], max_length=100),
        ),
    ]