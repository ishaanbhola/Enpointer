# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-27 09:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dragonslayer', '0026_auto_20170927_0933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='uid',
        ),
    ]
