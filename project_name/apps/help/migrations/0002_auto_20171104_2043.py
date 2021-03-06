# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-04 20:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import project_name.apps.core.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('help', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='help',
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='help',
            name='created_by',
            field=project_name.apps.core.utils.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='help_help_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='help',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created'),
        ),
        migrations.AddField(
            model_name='help',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='date modified'),
        ),
        migrations.AddField(
            model_name='help',
            name='is_deleted',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='help',
            name='modified_by',
            field=project_name.apps.core.utils.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='help_help_modified_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
