# coding=utf-8
# author= YQZHU

from django.conf.urls import url, include
from . import client_views

urlpatterns = [
    url(r'^$', client_views.list_clients, name='list_clients'),
url(r'^myclients$', client_views.my_clients, name='my_clients'),
    url(r'^add_client', client_views.add_client, name='add_client'),
    url(r'^edit_client/(?P<id>[0-9]+)/$', client_views.edit_client, name='edit_client'),
    url(r'^view_client/(?P<id>[0-9]+)/$', client_views.view_client, name='view_client'),

    # SKU
    ]