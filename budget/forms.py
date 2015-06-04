from django.forms import ModelForm
from budget.models import Account

class NewAccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'bank', 'acc_type', 'balance']
