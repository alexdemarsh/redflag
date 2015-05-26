# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='contents',
        ),
        migrations.AddField(
            model_name='data',
            name='docfile',
            field=models.FileField(default=b'', upload_to=b'documents/%Y/%m/%d'),
        ),
    ]
