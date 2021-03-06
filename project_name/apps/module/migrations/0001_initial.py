# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('match', models.CharField(default='#', max_length=200)),
                ('reference', models.CharField(max_length=100, unique=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': '1. Modules',
                'ordering': ['order'],
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ModuleItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('match', models.CharField(default='#', max_length=200)),
                ('reference', models.CharField(max_length=100, unique=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': '2. Module Items',
                'ordering': ['module'],
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='RoleModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
            ],
            options={
                'verbose_name_plural': '3. Module Teams',
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='RoleModuleItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
            ],
            options={
                'verbose_name_plural': '4. Module Item Teams',
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
    ]
