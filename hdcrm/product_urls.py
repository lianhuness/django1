# coding=utf-8
# author= YQZHU

from django.conf.urls import url, include
from . import powerband_views, product_views, caigou_views, latexband_views, otherproduct_views


urlpatterns = [
    # url(r'^list_products', product_views.list_products, name='list_products'),
    url(r'^list_products$', product_views.list_products, name='list_products'),
    url(r'^list_products/(?P<product_type>\w+)/$', product_views.list_products, name='list_products_type'),

    url(r'^view_product/(?P<id>[0-9]+)/$', product_views.view_product, name='view_product'),
    url(r'^edit_product/(?P<id>[0-9]+)/$', product_views.edit_product, name='edit_product'),
    url(r'^delete_product/(?P<id>[0-9]+)/$', product_views.delete_product, name='delete_product'),

    url(r'^add_powerband', powerband_views.add, name='add_powerband'),
    url(r'^edit_powerband/(?P<id>[0-9]+)/$', powerband_views.edit, name='edit_powerband'),

    url(r'^add_supplier', caigou_views.add_supplier, name='add_supplier'),
    url(r'^add_caigou', caigou_views.add_caigou, name='add_caigou'),
    url(r'^edit_caigou/(?P<id>[0-9]+)/$', caigou_views.edit, name='edit_caigou'),


    url(r'^add_latexband', latexband_views.add, name='add_latexband'),
    url(r'^edit_latexband/(?P<id>[0-9]+)/$', latexband_views.edit, name='edit_latexband'),

    # Otherproduct_views   OtherProduct
url(r'^add_otherlatex', otherproduct_views.add_otherlatex, name='add_otherlatex'),
    url(r'^edit_otherlatex/(?P<id>[0-9]+)/$', otherproduct_views.edit_otherlatex, name='edit_otherlatex'),
    # Otherproduct_view PVC
url(r'^add_pvc', otherproduct_views.add_pvc, name='add_pvc'),
    url(r'^edit_pvc/(?P<id>[0-9]+)/$', otherproduct_views.edit_pvc, name='edit_pvc'),
    # Otherproduct Others
url(r'^add_other', otherproduct_views.add_other, name='add_other'),
    url(r'^edit_other/(?P<id>[0-9]+)/$', otherproduct_views.edit_other, name='edit_other'),
]
