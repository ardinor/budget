from django.conf.urls import patterns, url

from budget import views

urlpatterns = patterns('',
    # /budget
    url(r'^$', views.index, name='index'),
    # /budget/transactions/
    url(r'^transactions/$', views.transaction_list, name='transaction_list'),
    # /budget/transaction/<number>
    url(r'^transaction/(?P<transaction_id>\d+)/$', views.transaction_detail, name='transaction_detail'),
    # /budget/accounts/
    url(r'^accounts/$', views.account_list, name='account_list'),
    # /budget/accounts/<number>
    url(r'^accounts/(?P<account_id>\d+)/$', views.account_transactions, name='account_transactions'),
    # /budget/transaction/new
    url(r'^transaction/new/$', views.transaction_new, name='transaction_new'),
    # /budget/transaction/save
    url(r'^transaction/save/$', views.transaction_save, name='transaction_save'),
)
