# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170919_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='default string'),
            preserve_default=False,
        ),
    ]