# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-05 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dragonslayer', '0036_auto_20170929_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomFieldValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('val_char', models.CharField(blank=True, max_length=100, null=True)),
                ('val_int', models.IntegerField(blank=True, null=True)),
                ('val_boolean', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('titile', models.CharField(blank=True, max_length=100, null=True)),
                ('value', models.CharField(blank=True, max_length=100, null=True)),
                ('default', models.BooleanField(default=False)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Org')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Project')),
            ],
        ),
        migrations.AddField(
            model_name='customfield',
            name='field_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='epic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='dragonslayer.Issue'),
        ),
        migrations.AddField(
            model_name='customfieldvalue',
            name='custom_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.CustomField'),
        ),
        migrations.AddField(
            model_name='customfieldvalue',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Issue'),
        ),
        migrations.AddField(
            model_name='customfieldvalue',
            name='val_options',
            field=models.ManyToManyField(to='dragonslayer.Option'),
        ),
    ]