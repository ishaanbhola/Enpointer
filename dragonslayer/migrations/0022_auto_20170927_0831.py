# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-27 08:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dragonslayer', '0021_issue_sprint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('min_issues', models.IntegerField(blank=True, null=True)),
                ('max_issues', models.IntegerField(blank=True, null=True)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Org')),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Org')),
            ],
        ),
        migrations.CreateModel(
            name='CustomField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Org')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('org', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Org')),
            ],
        ),
        migrations.CreateModel(
            name='IssueType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Org')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Org')),
            ],
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Org')),
            ],
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('issue_types', models.ManyToManyField(to='dragonslayer.IssueType')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Org')),
            ],
        ),
        migrations.CreateModel(
            name='Transition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('released', models.BooleanField(default=False)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Org')),
            ],
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Org')),
            ],
        ),
        migrations.RemoveField(
            model_name='epic',
            name='org',
        ),
        migrations.RemoveField(
            model_name='epic',
            name='project',
        ),
        migrations.RemoveField(
            model_name='story',
            name='epic',
        ),
        migrations.RemoveField(
            model_name='story',
            name='org',
        ),
        migrations.RemoveField(
            model_name='story',
            name='project',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='epic',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='story',
        ),
        migrations.AddField(
            model_name='project',
            name='admin',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sprint',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sprint',
            name='goal',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='status',
            name='resolution',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Priority'),
        ),
        migrations.DeleteModel(
            name='Epic',
        ),
        migrations.DeleteModel(
            name='Story',
        ),
        migrations.AddField(
            model_name='workflow',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Project'),
        ),
        migrations.AddField(
            model_name='version',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Project'),
        ),
        migrations.AddField(
            model_name='transition',
            name='end_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Status'),
        ),
        migrations.AddField(
            model_name='transition',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Org'),
        ),
        migrations.AddField(
            model_name='transition',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Project'),
        ),
        migrations.AddField(
            model_name='transition',
            name='start_status',
            field=models.ManyToManyField(related_name='transitions', to='dragonslayer.Status'),
        ),
        migrations.AddField(
            model_name='screen',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Project'),
        ),
        migrations.AddField(
            model_name='screen',
            name='transition',
            field=models.ManyToManyField(related_name='screens', to='dragonslayer.Transition'),
        ),
        migrations.AddField(
            model_name='priority',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Project'),
        ),
        migrations.AddField(
            model_name='label',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Project'),
        ),
        migrations.AddField(
            model_name='issuetype',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Project'),
        ),
        migrations.AddField(
            model_name='customfield',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Project'),
        ),
        migrations.AddField(
            model_name='customfield',
            name='screen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Screen'),
        ),
        migrations.AddField(
            model_name='component',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Project'),
        ),
        migrations.AddField(
            model_name='column',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Project'),
        ),
        migrations.AddField(
            model_name='issue',
            name='affected_version',
            field=models.ManyToManyField(blank=True, null=True, to='dragonslayer.Version'),
        ),
        migrations.AddField(
            model_name='issue',
            name='component',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Component'),
        ),
        migrations.AddField(
            model_name='issue',
            name='fix_version',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='dragonslayer.Version'),
        ),
        migrations.AddField(
            model_name='issue',
            name='issue_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.IssueType'),
        ),
        migrations.AddField(
            model_name='issue',
            name='label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Label'),
        ),
        migrations.AddField(
            model_name='status',
            name='column',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dragonslayer.Column'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='group',
            field=models.ManyToManyField(blank=True, null=True, to='dragonslayer.Group'),
        ),
    ]