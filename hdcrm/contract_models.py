# coding=utf-8
# author= YQZHU


from django.db import models
from .user_models import Sales
from .client_models import Client
from .sku_models import Sku


CURRENCY_CHOICE=(
    ( 'RMB', 'RMB'),
    ('USD', 'USD')
)

from django.db.models import Sum

import pdb
class Contract(models.Model):
    sales = models.ForeignKey(Sales)
    client = models.ForeignKey(Client)
    orderNumber = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(max_length=5, choices=CURRENCY_CHOICE, default='RMB')
    deliveryDate = models.DateField()
    hetong = models.FileField(upload_to='contracts/hetong', blank=True, null=True)

    def __str__(self):
        return self.orderNumber

    def total(self):
        return self.contractsku_set.aggregate(Sum('total'))['total__sum']

    def income(self):
        return self.contractincome_set.aggregate(Sum('amount'))['amount__sum']

    def expense(self):
        return self.contractexpense_set.aggregate(Sum('amount'))['amount__sum']


class ContractSku(models.Model):
    contract = models.ForeignKey(Contract)
    sku = models.ForeignKey(Sku)
    qty = models.PositiveIntegerField(default=0)
    unitcost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total =  models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return "%s: %s" %(self.contract, self.sku)


from django import forms

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ('sales', 'client', 'orderNumber', 'amount', 'currency', 'deliveryDate' ,'hetong')
        labels={
            'orderNumber': u'订单号',
            'amount': u'总金额',
            'currency': u'币种',
            'sales': u'销售员',
            'deliveryDate': u'交货日期',
            'hetong': u'合同文件',
        }

    def __init__(self, *args,**kwargs):
        super(ContractForm, self).__init__(*args, **kwargs)
        self.fields['client'].widget = forms.HiddenInput()

class ContractSkuForm(forms.ModelForm):
    class Meta:
        model = ContractSku
        fields=('contract', 'sku', 'qty', 'unitcost','total')
        labels={
            'contract': u'合同编号',
            'sku': u'SKU',
            'qty': u'数量',
            'unitcost': u'单价',
            'total': u'金额'
        }

    def __init__(self, *args, **kwargs):
        super(ContractSkuForm, self).__init__(*args, **kwargs)
        self.fields['contract'].widget=forms.HiddenInput()



class ContractIncome(models.Model):
    contract = models.ForeignKey(Contract)
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(max_length=5, choices=CURRENCY_CHOICE, default='RMB')
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return u"%s %s(%s)"%(self.source, self.amount, self.currency)

class ContractIncomeForm(forms.ModelForm):
    class Meta:
        model = ContractIncome
        fields = ('contract', 'source', 'amount', 'currency')
        labels={
            'contract': u'合同',
            'source': u'账户',
            'amount': u'金额',
            'currency': u'货币'
        }
    def __init__(self, *args, **kwargs):
        super(ContractIncomeForm, self).__init__(*args, **kwargs)
        self.fields['contract'].widget = forms.HiddenInput()


class ContractExpense(models.Model):
    contract = models.ForeignKey(Contract)
    topic = models.CharField(max_length=100)
    payto = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(max_length=5, choices=CURRENCY_CHOICE, default='RMB')
    document = models.FileField(upload_to='contracts/expense')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"%s %s(%s)"%(self.payto, self.amount, self.currency)

class ContractExpenseForm(forms.ModelForm):
    class Meta:
        model = ContractExpense
        fields = ('topic', 'contract', 'payto', 'amount', 'currency', 'document')
        labels={
            'topic': u'主题',
            'contract': u'合同',
            'payto': u'对方账户',
            'amount': u'金额',
            'currency': u'货币',
            'document': u'发票'
        }
    def __init__(self, *args, **kwargs):
        super(ContractExpenseForm, self).__init__(*args, **kwargs)
        self.fields['contract'].widget = forms.HiddenInput()