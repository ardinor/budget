from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from budget.models import Account

class NewAccountForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewAccountForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'budget:account_save'

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = Account
        fields = ['name', 'bank', 'acc_type', 'balance']
