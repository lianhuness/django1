# coding=utf-8
# author= YQZHU

from django.conf.urls import url, include
from . import user_views

urlpatterns = [
    url(r'^listusers', user_views.listusers, name='listusers'),
    url(r'^add_sales', user_views.add_sales, name='add_sales'),
    url(r'^login_user', user_views.login_user, name='login_user'),
    url(r'^logout_user', user_views.logout_user, name='logout_user'),
    ]