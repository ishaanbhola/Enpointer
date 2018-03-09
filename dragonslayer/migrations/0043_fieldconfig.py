# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-11 11:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dragonslayer', '0042_auto_20171011_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title_required', models.BooleanField(default=False)),
                ('title_visible', models.BooleanField(default=True)),
                ('title_text', models.CharField(blank=True, max_length=100, null=True)),
                ('description_required', models.BooleanField(default=False)),
                ('description_visible', models.BooleanField(default=True)),
                ('description_text', models.CharField(blank=True, max_length=100, null=True)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Org')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Project')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Screen')),
            ],
        ),
    ]
