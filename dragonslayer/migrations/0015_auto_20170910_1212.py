# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-10 12:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dragonslayer', '0014_userprofile_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='org',
            name='sections',
        ),
        migrations.RemoveField(
            model_name='project',
            name='issues',
        ),
        migrations.RemoveField(
            model_name='section',
            name='projects',
        ),
        migrations.AddField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Issue'),
        ),
        migrations.AddField(
            model_name='issue',
            name='org',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Org'),
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Project'),
        ),
        migrations.AddField(
            model_name='project',
            name='org',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Org'),
        ),
        migrations.AddField(
            model_name='project',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Section'),
        ),
        migrations.AddField(
            model_name='section',
            name='org',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Org'),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='org',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='org',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Org'),
        ),
    ]