# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 23:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import project_name.apps.core.utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('periods', models.IntegerField()),
                ('contractor', models.CharField(max_length=100)),
                ('resident', models.CharField(max_length=100)),
                ('supervisor', models.CharField(max_length=100)),
                ('execution_time', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('created_by', project_name.apps.core.utils.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_project_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', project_name.apps.core.utils.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_project_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Project',
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('name',)]),
        ),
    ]
