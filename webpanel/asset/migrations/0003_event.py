# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_auto_20170918_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('type', models.CharField(max_length=256)),
                ('event_data', models.CharField(max_length=256)),
            ],
        ),
    ]
