# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-12-03 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_user',
            name='book',
            field=models.CharField(max_length=100),
        ),
    ]
