import locale

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Reasons(models.Model):
    reason_desc = models.CharField(max_length=200)

    @python_2_unicode_compatible
    def __str__(self):
        return self.reason_desc


class AccountTypes(models.Model):
    type_name = models.CharField(max_length=100)

    @python_2_unicode_compatible
    def __str__(self):
        return self.type_name


# Savings, Transaction etc.
class Account(models.Model):
    type = models.ForeignKey(AccountTypes)
    name = models.CharField(max_length=100)
    bank = models.CharField(max_length=100)

    @python_2_unicode_compatible
    def __str__(self):
        return '%s account "%s"' % (self.type, self.name)


# Date, Debit, Credit, Reason, Account
class Transaction(models.Model):

    DEBIT_TRANSACTION = 'DB'
    CREDIT_TRANSACTION = 'CR'
    TRANSACTION_TYPES = (
        (DEBIT_TRANSACTION, 'Debit'),
        (CREDIT_TRANSACTION, 'Credit'),
    )

    date = models.DateTimeField('Date')
    type = models.CharField(max_length=2, choices=TRANSACTION_TYPES,
        default=DEBIT_TRANSACTION)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.ForeignKey(Reasons)
    reason_other = models.CharField(max_length=200)
    account = models.ForeignKey(Account)

    @python_2_unicode_compatible
    def __str__(self):
        return '%s - %s of %d' % (self.date.strftime('%m/%d/%Y'),
            self.type,
            locale.currency(self.amount))
