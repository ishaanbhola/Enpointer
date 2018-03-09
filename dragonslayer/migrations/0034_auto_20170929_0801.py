# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-29 08:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dragonslayer', '0033_transition_workflow'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionscreenscheme',
            name='org',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Org'),
        ),
        migrations.AddField(
            model_name='actionscreenscheme',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Project'),
        ),
        migrations.AddField(
            model_name='actionscreenscheme',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='actionscreenscheme',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]