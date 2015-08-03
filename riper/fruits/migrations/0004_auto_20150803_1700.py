# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('fruits', '0003_auto_20150803_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='url',
            field=models.CharField(validators=[django.core.validators.URLValidator()], max_length=50, default='Wiki-page'),
        ),
    ]
