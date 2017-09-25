# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20170917_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='tg_username',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tg_user_id',
            field=models.CharField(blank=True, max_length=64, verbose_name='ID в Telegram (брать здесь: https://t.me/userinfobot)'),
        ),
    ]