# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-30 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flixx', '0006_remove_genre_a'),
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Budget', models.IntegerField()),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=200)),
                ('overview', models.CharField(max_length=1000)),
                ('dateofrelease', models.DateField()),
                ('popularity', models.DecimalField(decimal_places=4, max_digits=100)),
                ('revenue', models.IntegerField()),
                ('runtime', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
                ('tag', models.CharField(max_length=500)),
                ('averagerating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('nutr', models.IntegerField()),
                ('genres', models.ManyToManyField(to='flixx.Genre')),
            ],
        ),
    ]
