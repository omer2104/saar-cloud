# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CloudUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('displayName', models.CharField(max_length=100)),
                ('directory', models.CharField(max_length=10000)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
