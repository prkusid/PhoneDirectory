# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-04-02 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhoneDirectory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonedirectory',
            name='phone_no',
            field=models.IntegerField(max_length=10),
        ),
    ]
