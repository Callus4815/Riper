# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fruits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruit',
            name='url',
            field=models.CharField(default='none', max_length=50),
        ),
    ]
