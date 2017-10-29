# coding=utf-8
# author= YQZHU

from django.conf.urls import url, include


urlpatterns = [
    url(r'^user/', include('hdcrm.user_urls')),
    url(r'^client/', include('hdcrm.client_urls')),
    url(r'^product/', include('hdcrm.product_urls')),
    url(r'^sku/', include('hdcrm.sku_urls')),
url(r'^contract/', include('hdcrm.contract_urls')),

]


