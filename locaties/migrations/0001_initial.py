# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-07 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[(b'K', b'Kerd'), (b'C', b'Crematorium'), (b'A', b'Aula')], default=b'K', max_length=1)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
