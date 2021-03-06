# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 14:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import project_name.apps.core.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostoPre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('periodo', models.CharField(max_length=100)),
                ('valor_planificado', models.TextField()),
                ('valor_ganado', models.IntegerField()),
                ('valor_real', models.CharField(max_length=100)),
                ('created_by', project_name.apps.core.utils.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_costopre_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', project_name.apps.core.utils.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_costopre_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CostoPre',
                'verbose_name_plural': 'CostoPre',
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='costopre',
            name='projecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project'),
        ),
        migrations.AlterUniqueTogether(
            name='costopre',
            unique_together=set([('periodo',)]),
        ),
    ]
