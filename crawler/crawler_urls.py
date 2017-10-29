# coding=utf-8
# author= YQZHU

from django.conf.urls import url, include
from . import crawler_views



urlpatterns = [
    url(r'^keywords$', crawler_views.list_keywords.as_view(), name='keywords-list'),
    url(r'^keywords/add$', crawler_views.keyword_add.as_view(), name='keyword-add'),
    url(r'keyword/(?P<pk>[0-9]+)/delete/$', crawler_views.keyword_delete.as_view(), name='keyword-delete'),
    ]