# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plugin_app_db',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'plugin_app_db',
            },
        ),
        migrations.CreateModel(
            name='Plugin_db',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plugin_name', models.CharField(max_length=100)),
                ('plugin_content', models.CharField(max_length=200, null=True)),
                ('plugin_version', models.CharField(max_length=100, null=True)),
                ('plugin_filedir', models.CharField(max_length=100)),
                ('plugin_vultype', models.CharField(max_length=100, null=True)),
                ('plugin_app', models.ForeignKey(to='pocManageApp.Plugin_app_db')),
            ],
            options={
                'db_table': 'plugin_db',
            },
        ),
    ]
