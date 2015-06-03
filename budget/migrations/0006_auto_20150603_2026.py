# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0005_account_balance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='type',
            new_name='acc_type',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='type',
            new_name='trans_type',
        ),
    ]
