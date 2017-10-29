# coding=utf-8
# author= YQZHU
from django.conf.urls import url, include
from . import donwoo_views
from . import sku_views

urlpatterns = [
    url(r'^$', donwoo_views.index, name='donwoo_home'),
    url(r'^search/(?P<search_type>\w+)$', donwoo_views.search, name='donwoo_search'),

    url(r'^skugroup/add$', sku_views.add_skugroup, name='add_skugroup'),
    url(r'^skugroup/(?P<pk>[0-9]+)$', sku_views.view_skugroup, name='view_skugroup'),
    url(r'^skugroup/(?P<pk>[0-9]+)/edit$', sku_views.edit_skugroup, name='edit_skugroup'),
    url(r'^skugroup/(?P<pk>[0-9]+)/delete', sku_views.delete_skugroup, name='del_skugroup'),

    url(r'^sku/add$', sku_views.dw_add_sku , name='dw_add_sku'),
    url(r'^sku/add/(?P<sg>[0-9]+)$', sku_views.dw_add_sku , name='dw_add_sku_sg'),
    url(r'^sku/(?P<pk>[0-9]+)$', sku_views.view_sku , name='dw_view_sku'),
    url(r'^sku/(?P<pk>[0-9]+)/edit$', sku_views.edit_sku , name='dw_edit_sku'),
    url(r'^sku/(?P<pk>[0-9]+)/delete', sku_views.delete_sku , name='dw_delete_sku'),

    # # SKU Image
    # url(r'^sku/(?P<pk>[0-9]+)/addimage', sku_views.dw_add_skuimage, name='dw_add_skuimage'),
    # url(r'^skuimg/(?P<pk>[0-9]+)/delete', sku_views.dw_delete_skuimg , name='dw_delete_skuimg'),

    # SKU File
    url(r'^sku/(?P<pk>[0-9]+)/addfile', sku_views.dw_add_skufile, name='dw_add_skufile'),
    url(r'^skufile/(?P<pk>[0-9]+)/delete', sku_views.dw_delete_skufile , name='dw_delete_skufile'),

    # SKU  Quote
    url(r'^sku/(?P<pk>[0-9]+)/addquote', sku_views.dw_add_skuquote, name='dw_add_skuquote'),
    url(r'^skuquote/(?P<pk>[0-9]+)/delete', sku_views.dw_delete_skuquote , name='dw_delete_skuquote'),
    ]