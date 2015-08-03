# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('fruits', '0002_fruit_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='url',
            field=models.CharField(default='none', max_length=50, validators=[django.core.validators.URLValidator()]),
        ),
    ]
