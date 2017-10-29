# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 16:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hdcrm', '0003_auto_20171006_2206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Powerband',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.DecimalField(decimal_places=2, max_digits=10)),
                ('phantom', models.CharField(max_length=20)),
                ('color', models.CharField(choices=[('RED', '红'), ('ORANGE', '橙'), ('YELLOW', '黄'), ('GREEN', '绿'), ('BLUE', '蓝'), ('BLACK', '黑'), ('PURPLE', '紫'), ('PINK', '粉'), ('NOCOLOR', '本色')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('type', models.CharField(choices=[('POWERBAND208', '208圈'), ('POWERBAND101', '101圈'), ('5060MINIBAND', '50/60cm小圈')], max_length=100)),
                ('weight', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='powerband',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hdcrm.Product'),
        ),
    ]