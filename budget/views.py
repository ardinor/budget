from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from budget.models import Account, Transaction, Reasons

def index(request):
    latest_transactions = Transaction.objects.order_by('-date')[:10]
    context = {'latest_transactions': latest_transactions}
    return render(request, 'budget/index.html', context)

def transaction_list(request):
    latest_transactions = Transaction.objects.order_by('-date')[:20]
    context = {'latest_transactions': latest_transactions}
    return render(request, 'budget/transaction_list.html', context)

def transaction_detail(request, transaction_id):
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
        new_trans
    except (KeyError):
        return render(request, 'budget/transaction_new.html',
            {'error_message': 'Error'})
    return HttpResponseRedirect(reverse('budget:transaction_detail',
        args=(new_trans.id,)))

def account_list(request):
    account_list = Account.objects.all()
    context = {'accounts': account_list}
    return render(request, 'budget/account_list.html', context)

def account_transactions(request, account_id):
    # Lists all the transactions for an account, use the name in the URL
    # or the DB ID?
    return render(request, 'budget/account_transactions.html')

def account_new(request):
    return render(request, 'budget/account_new.html')

def account_save(request):
    pass

def reason_list(request):
    reasons = Reasons.objects.all()
    context = {'reasons': reasons}
    return render(request, 'budget/reason_list.html', context)

def reason_new(request):
    return render(request, 'budget/reason_new.html')

def reason_save(request):
    pass
