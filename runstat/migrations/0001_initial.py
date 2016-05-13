# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 11:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.BigIntegerField(unique=True, verbose_name='member object id')),
                ('name', models.CharField(max_length=256, verbose_name='member name')),
                ('administrator', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='GroupPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.CharField(max_length=100, unique=True, verbose_name='post object id')),
                ('message', models.TextField(blank=True, null=True, verbose_name='post message')),
                ('tags', models.CharField(default='', max_length=4096, null=True, verbose_name='tags in post')),
                ('created_time', models.DateTimeField(verbose_name='post created time')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='runstat.GroupMember', verbose_name='post author')),
            ],
        ),
        migrations.CreateModel(
            name='PostPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.BigIntegerField(unique=True, verbose_name='post object id')),
                ('url_native', models.URLField(max_length=1000)),
                ('url_x600', models.URLField(max_length=1000)),
                ('url_x480', models.URLField(max_length=1000)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runstat.GroupPost', verbose_name='post')),
            ],
        ),
    ]
