# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20161027_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicecredentials',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
