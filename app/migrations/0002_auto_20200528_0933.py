# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-05-28 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adicionaldeservico',
            name='is_approved',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='servico',
            name='is_approved',
            field=models.BooleanField(default=True),
        ),
    ]