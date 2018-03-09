# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-09 10:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dragonslayer', '0007_auto_20170909_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Section'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sections',
            field=models.ManyToManyField(to='dragonslayer.Section'),
        ),
    ]