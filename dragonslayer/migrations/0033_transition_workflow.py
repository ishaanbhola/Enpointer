# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-29 07:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dragonslayer', '0032_userprofile_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='transition',
            name='workflow',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Workflow'),
        ),
    ]
