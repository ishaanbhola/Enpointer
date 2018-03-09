# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-12 15:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dragonslayer', '0046_auto_20171012_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customfield',
            name='options',
        ),
        migrations.AddField(
            model_name='option',
            name='custom_field',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.CustomField'),
        ),
    ]