# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-18 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunknightsapp', '0010_auto_20170216_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='clanuser',
            name='country_tag',
            field=models.CharField(default='red-cross', max_length=10),
        ),
    ]
