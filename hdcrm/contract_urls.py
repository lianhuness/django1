# coding=utf-8
# author= YQZHU

from django.conf.urls import url, include
from . import contract_views


urlpatterns=[
    url(r'^$', contract_views.list_contracts, name='list_contracts'),
    url(r'^mine$', contract_views.list_contracts, name='my_contracts'),
    url(r'^add_contract/(?P<cid>[0-9]+)/$', contract_views.add_contract, name='add_contract'),
    url(r'^(?P<id>[0-9]+)/$', contract_views.view_contract , name='view_contract'),
    url(r'^edit_contract/(?P<id>[0-9]+)/$', contract_views.edit_contract, name='edit_contract'),
    url(r'^add_contractsku/(?P<id>[0-9]+)/$', contract_views.add_contractsku, name='add_contractsku'),
    url(r'^delete_contractsku/(?P<id>[0-9]+)/$', contract_views.delete_contractsku, name='delete_contractsku'),

    url(r'^add_income/(?P<cid>[0-9]+)/$', contract_views.add_income, name='add_income'),
    url(r'^view_incomes/(?P<cid>[0-9]+)/$', contract_views.view_incomes, name='view_incomes'),
    url(r'^delete_income/(?P<id>[0-9]+)/$', contract_views.delete_income, name='delete_income'),


    url(r'^add_expense/(?P<cid>[0-9]+)/$', contract_views.add_expense, name='add_expense'),
    url(r'^view_expenses/(?P<cid>[0-9]+)/$', contract_views.view_expenses, name='view_expenses'),
    url(r'^delete_expense/(?P<id>[0-9]+)/$', contract_views.delete_expense, name='delete_expense'),
]