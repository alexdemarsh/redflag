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
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('contents', models.TextField()),
                ('version', models.IntegerField()),
                ('owner', models.ForeignKey(related_name='data_requests_created', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Math',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('language', models.CharField(max_length=10, choices=[(b'R', b'R'), (b'Python', b'Python'), (b'SAS', b'SAS'), (b'STATA', b'STATA'), (b'Julia', b'Julia')])),
                ('code', models.TextField()),
                ('version', models.IntegerField()),
                ('owner', models.ForeignKey(related_name='math_requests_created', to=settings.AUTH_USER_MODEL)),
                ('related_data', models.ManyToManyField(related_name='math_requests_created', to='repository.Data')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
