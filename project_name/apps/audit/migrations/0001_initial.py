# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CRUDEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.SmallIntegerField(choices=[(1, 'Create'), (2, 'Update'), (3, 'Delete'), (4, 'Many-to-Many Change'), (5, 'Reverse Many-to-Many Change')])),
                ('object_id', models.IntegerField()),
                ('object_repr', models.CharField(blank=True, max_length=255, null=True)),
                ('object_json_repr', models.TextField(blank=True, null=True)),
                ('user_pk_as_string', models.CharField(blank=True, help_text='String version of the user pk', max_length=255, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'CRUD event',
                'verbose_name_plural': 'CRUD events',
                'ordering': ['-datetime'],
            },
        ),
        migrations.CreateModel(
            name='LoginEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_type', models.SmallIntegerField(choices=[(0, 'Login'), (1, 'Logout'), (2, 'Failed login')])),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'login event',
                'verbose_name_plural': 'login events',
                'ordering': ['-datetime'],
            },
        ),
    ]
