# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-05-23 23:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200522_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='contratodeservico',
            name='motivo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
