# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 11:25
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import project_name.apps.core.manager
import project_name.apps.core.utils.fields
import project_name.apps.core.utils.upload_folder
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('ubigeo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('username', models.CharField(help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=40, null=True)),
                ('last_name', models.CharField(blank=True, max_length=40, null=True)),
                ('display_name', models.CharField(blank=True, max_length=14, null=True, verbose_name='display name')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_invited', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'auth_user',
                'abstract': False,
                'swappable': 'user.User',
            },
            managers=[
                ('objects', project_name.apps.core.manager.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('document_type', models.CharField(blank=True, choices=[('', '--Choose--'), ('PERS-1', 'Natural'), ('PERS-2', 'Legal')], max_length=10, null=True)),
                ('document_number', models.CharField(blank=True, max_length=20, null=True)),
                ('trade_name', models.CharField(blank=True, max_length=255, null=True, verbose_name=' trade_name')),
                ('contributor_type', models.CharField(blank=True, max_length=80, null=True, verbose_name='contributor_type')),
                ('status_contributor', models.CharField(blank=True, max_length=80, null=True, verbose_name='status_contributor')),
                ('condition', models.CharField(blank=True, max_length=80, null=True, verbose_name='condition')),
                ('address_fiscal', models.CharField(blank=True, max_length=255, null=True, verbose_name='address_fiscal')),
                ('affiliate_ple', models.CharField(blank=True, max_length=255, null=True, verbose_name='affiliate_ple')),
                ('padrones', models.CharField(blank=True, max_length=255, null=True, verbose_name='padrones')),
            ],
            options={
                'verbose_name': 'User Company',
                'verbose_name_plural': 'Users Company',
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_userprofile_user', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('gender_type', models.CharField(blank=True, choices=[('', '--Choose--'), ('GEN-1', 'Male'), ('GEN-2', 'Female')], max_length=10, null=True)),
                ('home_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('logo_profile', models.ImageField(blank=True, null=True, upload_to=project_name.apps.core.utils.upload_folder.upload_user_profile)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_userprofile_city', to='ubigeo.City', verbose_name='city')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_userprofile_country', to='ubigeo.Country', verbose_name='country')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'db_table': 'user_profile',
            },
            managers=[
                ('current', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='usercompany',
            name='created_by',
            field=project_name.apps.core.utils.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_usercompany_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usercompany',
            name='modified_by',
            field=project_name.apps.core.utils.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_usercompany_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usercompany',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_usercompany_user', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='user',
            name='team',
            field=models.ManyToManyField(blank=True, related_name='team', to='core.Team', verbose_name='teams'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='created_by',
            field=project_name.apps.core.utils.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_userprofile_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='modified_by',
            field=project_name.apps.core.utils.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_userprofile_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='space_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_userprofile_space_plan', to='core.SpacePlans'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_userprofile_state', to='ubigeo.State', verbose_name='state'),
        ),
        migrations.AlterUniqueTogether(
            name='usercompany',
            unique_together=set([('user', 'document_type', 'document_number')]),
        ),
    ]
