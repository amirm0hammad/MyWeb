# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-07 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.AlterField(
            model_name='users',
            name='User_name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
