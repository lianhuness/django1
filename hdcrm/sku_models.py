# coding=utf-8
# author= YQZHU

from django.contrib.auth.models import User
from django.db import models
from .client_models import Client
from .product_models import Product

from .powerband_models import Powerband
from .caigou_models import Caigou
from .latexband_models import LatexBand
from .otherproduct_models import OtherLatex, Pvc, OtherProduct

CURRENCY_CHOICE=(
    ('USD', u'美金'),
    ('CNY', u'人民币')
)
class Sku(models.Model):
    user = models.ForeignKey(User)
    client = models.ForeignKey(Client)
    name = models.CharField(max_length=100, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    suggested_price = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    currency = models.CharField(max_length=5, choices=CURRENCY_CHOICE, default='CNY')

    def __str__(self):
        return "%s - %s" %(self.client, self.name)

class SkuItem(models.Model):
    sku = models.ForeignKey(Sku)
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField(default=1)
    note = models.TextField(blank=True, default='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u"%s - %s PCS - %s "%(self.product, self.quantity, self.note)


from django import forms

class SkuForm(forms.ModelForm):
    class Meta:
        model = Sku
        fields= ('user', 'client', 'name', 'suggested_price', 'currency')
        labels={
            'name': u'SKU昵称',
            'suggested_price': u'建议销售价格',
            'currency': u'货币'
        }

    def __init__(self, *args, **kwargs):
        super(SkuForm, self).__init__(*args, **kwargs)
        self.fields['client'].widget = forms.HiddenInput()
        self.fields['user'].widget = forms.HiddenInput()

class SkuItemForm(forms.ModelForm):
    class Meta:
        model = SkuItem
        fields=('sku', 'product', 'quantity', 'note')
        labels={
            'product': u'产品',
            'quantity': u'数量',
            'note': u'附注'
        }

    def __init__(self, *args,**kwargs):
        super(SkuItemForm, self).__init__(*args, **kwargs)
        self.fields['sku'].widget = forms.HiddenInput()

    def clean_product(self):
        product = self.cleaned_data['product']
        sku = self.cleaned_data['sku']
        if sku.skuitem_set.filter(product=product).exists():
            raise forms.ValidationError(u'此产品已经在这个SKU里， 不能重复添加')

        return product



