import locale

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Reasons(models.Model):
    reason_desc = models.CharField('Reason', max_length=200, unique=True)

    @python_2_unicode_compatible
    def __str__(self):
        return self.reason_desc

    class Meta:
        verbose_name = "Reason"
        verbose_name_plural = "Reasons"


class AccountTypes(models.Model):
    type_name = models.CharField('Account type', max_length=100, unique=True)

    @python_2_unicode_compatible
    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = "Account Type"
        verbose_name_plural = "Account Types"


# Savings, Transaction etc.
class Account(models.Model):
    type = models.ForeignKey(AccountTypes)
    name = models.CharField(max_length=100)
    bank = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    @python_2_unicode_compatible
    def __str__(self):
        return '%s account "%s"' % (self.type, self.name)

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"


# Date, Debit, Credit, Reason, Account
class Transaction(models.Model):

    DEBIT_TRANSACTION = 'DB'
    CREDIT_TRANSACTION = 'CR'
    TRANSACTION_TYPES = (
        (DEBIT_TRANSACTION, 'Debit'),
        (CREDIT_TRANSACTION, 'Credit'),
    )

    date = models.DateField('Date')
    type = models.CharField(max_length=2, choices=TRANSACTION_TYPES,
        default=DEBIT_TRANSACTION)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.ForeignKey(Reasons)
    reason_other = models.CharField(max_length=200, blank=True)
    account = models.ForeignKey(Account)

    @python_2_unicode_compatible
    def __str__(self):
        return '%s - %s of %s' % (self.date.strftime('%m/%d/%Y'),
            self.get_type_display(),
            locale.currency(self.amount))

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        ordering = ['-date']
