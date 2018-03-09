# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-26 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dragonslayer', '0081_issue_bg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='swimlane',
        ),
        migrations.AlterField(
            model_name='issue',
            name='current_time_estimate',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='original_time_estimate',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='timespent',
            field=models.TimeField(blank=True, null=True),
        ),
    ]