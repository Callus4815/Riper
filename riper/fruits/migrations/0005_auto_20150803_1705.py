# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fruits', '0004_auto_20150803_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='url',
            field=models.CharField(max_length=50, default='Wiki-page'),
        ),
    ]
