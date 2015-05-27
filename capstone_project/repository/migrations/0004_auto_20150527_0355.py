# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0003_auto_20150527_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='version',
            field=models.IntegerField(default=1),
        ),
    ]
