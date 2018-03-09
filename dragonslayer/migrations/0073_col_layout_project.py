# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-15 06:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dragonslayer', '0072_col_layout_width'),
    ]

    operations = [
        migrations.AddField(
            model_name='col_layout',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Project'),
        ),
    ]
