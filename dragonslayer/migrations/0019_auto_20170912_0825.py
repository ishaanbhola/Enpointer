# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-12 08:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dragonslayer', '0018_sprint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Org')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Project')),
            ],
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Status'),
        ),
    ]
