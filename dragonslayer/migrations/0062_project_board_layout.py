# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-08 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dragonslayer', '0061_auto_20171124_0645'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='board_layout',
            field=models.TextField(blank=True, null=True),
        ),
    ]
