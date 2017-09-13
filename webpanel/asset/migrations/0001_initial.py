# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 09:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('ipv4', models.CharField(db_index=True, max_length=15)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Актив',
                'verbose_name_plural': 'Активы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
            ],
            options={
                'verbose_name': 'Операционная система',
                'verbose_name_plural': 'Операционные системы',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='asset',
            name='os',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OperatingSystem', to='asset.OperatingSystem', verbose_name='Операционная система'),
        ),
    ]