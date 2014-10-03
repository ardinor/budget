# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_auto_20141003_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounttypes',
            name='type_name',
            field=models.CharField(max_length=100, verbose_name='Account type', unique=True),
        ),
        migrations.AlterField(
            model_name='reasons',
            name='reason_desc',
            field=models.CharField(max_length=200, verbose_name='Reason', unique=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
    ]
