from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from budget.models import Account, Transaction, Reasons, AccountTypes
from budget.forms import NewAccountForm

def index(request):
    latest_transactions = Transaction.objects.order_by('-date')[:10]
    return render(request, 'budget/index.html',
                  {'latest_transactions': latest_transactions})

def transaction_list(request):

    """
    Lists the first 20 available transactions for the user
    """

    latest_transactions = Transaction.objects.order_by('-date')[:20]
    return render(request, 'budget/transaction_list.html',
                  {'latest_transactions': latest_transactions})

def transaction_detail(request, transaction_id):

    """
    Gets details for the given transaction id, if it exists
    """

    transaction = get_object_or_404(Transaction, pk=transaction_id)
    return render(request, 'budget/transaction_detail.html',
        {'transaction': transaction})

def transaction_new(request):

    reasons = Reasons.objects
    accounts = Account.objects
    return render(request, 'budget/transaction_new.html',
                  {'reasons': reasons, 'accounts': accounts})

def transaction_save(request):
    try:
        date = request.POST['trans_date']
        amount = request.POST['trans_amount']
        type_db = request.POST['type_db']
        type_cr = request.POST['type_cr']
        desc = request.POST['trans_desc']
        acc = request.POST['trans_acc']
        new_trans = Transaction(date=date, )
    except (KeyError):
        return render(request, 'budget/transaction_new.html',
            {'error_message': 'Error'})
    return HttpResponseRedirect(reverse('budget:transaction_detail',
        args=(new_trans.id,)))

def account_list(request):
    account_list = Account.objects.all()
    return render(request, 'budget/account_list.html',
                  {'accounts': account_list})

def account_transactions(request, account_id):
    # Lists all the transactions for an account, use the name in the URL
    # or the DB ID?
    return render(request, 'budget/account_transactions.html')

def account_new(request):
    #account_types = AccountTypes.objects.all()
    form = NewAccountForm()
    return render(request, 'budget/account_new.html',
                  {'form': form})

def account_save(request):

    if request.method == 'POST':
        try:
            name = request.POST['acc_name']
            bank = request.POST['acc_bank']
            acc_type = request.POST['acc_type']
            amount = request.POST['acc_amount']
            new_accnt = Account(name=name, bank=bank, type=acc_type,
                                balance=amount)
        except (KeyError):
            return render(request, 'budget/account_new.html',
                {'error_message': 'Error'})
        # else:
        #     return render(request, 'budget/account_new.html',
        #                   {'error_message': 'Error'})

    return HttpResponseRedirect(reverse('budget:account_transactions',
        args=(new_accnt.id,)))

def reason_list(request):
    reasons = Reasons.objects.all()
    return render(request, 'budget/reason_list.html',
                  {'reasons': reasons})

def reason_new(request):
    return render(request, 'budget/reason_new.html')

def reason_save(request):
    pass
