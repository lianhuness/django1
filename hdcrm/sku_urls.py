# coding=utf-8
# author= YQZHU

from django.conf.urls import url, include
from . import sku_views

urlpatterns = [
    url(r'^$', sku_views.list_skus, name='list_skus'),
    url(r'^(?P<id>[0-9]+)/$', sku_views.view_sku , name='view_sku'),
    url(r'^add_sku/(?P<cid>[0-9]+)/$', sku_views.add_sku, name='add_sku'),
url(r'^edit_sku/(?P<id>[0-9]+)/$', sku_views.edit_sku, name='edit_sku'),

    url(r'^add_skuitem/(?P<sid>[0-9]+)/$', sku_views.add_skuitem, name='add_skuitem'),
url(r'^delete_skuitem/(?P<id>[0-9]+)/$', sku_views.del_skuitem, name='del_skuitem'),
    # url(r'^add_sku/(?P<id>[0-9]+)/$', sku_views.add_sku, name='add_sku'),
    # url(r'^edit_client/(?P<id>[0-9]+)/$', client_views.edit_client, name='edit_client'),
    # url(r'^view_client/(?P<id>[0-9]+)/$', client_views.view_client, name='view_client'),

    # SKU
    ]