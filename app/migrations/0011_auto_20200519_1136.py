# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-05-19 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200518_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='photo',
            field=models.URLField(blank=True, default='https://placehold.it/300x300', null=True),
        ),
        migrations.AlterField(
            model_name='fotoservico',
            name='url',
            field=models.URLField(blank=True, default='https://placehold.it/300x300', null=True),
        ),
        migrations.AlterField(
            model_name='profissional',
            name='photo',
            field=models.URLField(blank=True, default='https://placehold.it/300x300', null=True),
        ),
    ]
