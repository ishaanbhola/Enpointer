# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-07 23:51
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dragonslayer', '0003_auto_20170906_0043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('content', models.CharField(blank=True, max_length=500, null=True)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('commentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='assigned_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issues_assigned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='issue',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issues_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='issue',
            name='last_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Issue'),
        ),
    ]
