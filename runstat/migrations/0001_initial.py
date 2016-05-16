# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 17:35
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
                ('object_id', models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='member object id')),
                ('name', models.CharField(max_length=256, verbose_name='member name')),
                ('administrator', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='GroupPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.CharField(max_length=100, unique=True, verbose_name='post object id')),
                ('author', models.BigIntegerField(verbose_name='author object id')),
                ('message', models.TextField(blank=True, null=True, verbose_name='post message')),
                ('created_time', models.DateTimeField(verbose_name='post created time')),
                ('updated_time', models.DateTimeField(verbose_name='post updated time')),
            ],
        ),
        migrations.CreateModel(
            name='PostAttachments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, max_length=1000, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runstat.GroupPost', to_field='object_id', verbose_name='post id')),
            ],
        ),
    ]
