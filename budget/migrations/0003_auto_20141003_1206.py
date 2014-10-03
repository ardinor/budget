# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_auto_20141003_1202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name': 'Transaction', 'verbose_name_plural': 'Transactions', 'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='transaction',
            name='reason_other',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
