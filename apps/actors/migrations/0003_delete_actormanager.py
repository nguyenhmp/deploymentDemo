# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-25 00:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0002_actormanager'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ActorManager',
        ),
    ]
