# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(default='', blank=True, max_length=100)),
                ('description', models.TextField(default='', blank=True)),
                ('end', models.DateField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='', blank=True)),
                ('status', models.SmallIntegerField(default=1, choices=[(1, 'Not started'), (2, 'In progress'), (3, 'Testing'), (4, 'Done')])),
                ('order', models.SmallIntegerField(default=0)),
                ('started', models.DateField(blank=True, null=True)),
                ('due', models.DateField(blank=True, null=True)),
                ('completed', models.DateField(blank=True, null=True)),
                ('assigned', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('sprint', models.ForeignKey(blank=True, to='board.Sprint', null=True)),
            ],
        ),
    ]
