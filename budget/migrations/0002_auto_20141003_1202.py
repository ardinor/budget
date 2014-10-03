# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'Account', 'verbose_name_plural': 'Accounts'},
        ),
        migrations.AlterModelOptions(
            name='accounttypes',
            options={'verbose_name': 'Account Type', 'verbose_name_plural': 'Account Types'},
        ),
        migrations.AlterModelOptions(
            name='reasons',
            options={'verbose_name': 'Reason', 'verbose_name_plural': 'Reasons'},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name': 'Transaction', 'verbose_name_plural': 'Transactions'},
        ),
        migrations.AlterField(
            model_name='transaction',
            name='reason_other',
            field=models.CharField(null=True, max_length=200),
        ),
    ]
