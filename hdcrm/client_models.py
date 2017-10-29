# coding=utf-8
# author= YQZHU

from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from .user_models import Sales


class Client(models.Model):
    sales = models.ForeignKey(Sales)
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['sales', 'name', 'country', 'district']
        labels = {
            'sales': u'销售代表',
            'name':u'客户名称',
            'country': u'国家',
            'district': u'地区',
        }

