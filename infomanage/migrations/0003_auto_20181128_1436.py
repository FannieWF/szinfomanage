# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infomanage', '0002_auto_20181128_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kt',
            name='kt_name',
            field=models.CharField(max_length=100, verbose_name='\u8bfe\u9898\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='kt',
            name='school',
            field=models.CharField(max_length=70, verbose_name='\u6240\u5728\u5b66\u6821'),
        ),
    ]
