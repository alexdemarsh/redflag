# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0002_auto_20150526_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='docfile',
        ),
        migrations.AddField(
            model_name='data',
            name='url',
            field=models.URLField(default=b''),
        ),
    ]
