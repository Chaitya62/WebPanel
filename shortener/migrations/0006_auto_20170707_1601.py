# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-07 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_auto_20170707_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='shortUrl',
            field=models.URLField(max_length=100),
        ),
    ]
