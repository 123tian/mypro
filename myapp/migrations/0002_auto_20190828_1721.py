# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-28 09:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publisher',
            old_name='adddress',
            new_name='address',
        ),
    ]