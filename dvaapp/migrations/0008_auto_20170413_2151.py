# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0007_auto_20170413_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tevent',
            name='error_message',
            field=models.TextField(default=''),
        ),
    ]
