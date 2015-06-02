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
    # /budget/accounts/new
    url(r'^accounts/new/$', views.account_new, name='account_new'),
    # /budget/accounts/save
    url(r'^accounts/save/$', views.account_save, name='account_save'),
    # /budget/transaction/new
    url(r'^transaction/new/$', views.transaction_new, name='transaction_new'),
    # /budget/transaction/save
    url(r'^transaction/save/$', views.transaction_save, name='transaction_save'),
    # /reasons/
    url(r'^reasons/$', views.reason_list, name='reason_list'),
    # /reasons/new/
    url(r'^reasons/new/$', views.reason_new, name='reason_new'),
)
