# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-22 18:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item',
            new_name='item_creator',
        ),
    ]