# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-11 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0007_remove_comment_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='weblog.Post'),
        ),
    ]
