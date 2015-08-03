# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=25)),
                ('type', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
