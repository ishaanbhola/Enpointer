# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-26 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dragonslayer', '0093_auto_20180123_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
