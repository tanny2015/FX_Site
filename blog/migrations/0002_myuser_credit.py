# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='credit',
            field=models.IntegerField(default=0, verbose_name='积分'),
        ),
    ]