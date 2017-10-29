# coding=utf-8
# author= YQZHU


# coding=utf-8
# author= YQZHU

from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .product_models import  Product


class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ('name',)


class Caigou(Product):
    specs = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    supplier = models.ForeignKey(Supplier)
    def __str__(self):
        return self.name

    def kvs(self):
        kvs_data=[]
        kvs_data.append((u'供应商', self.supplier.name))
        kvs_data.append((u'规格', self.specs))
        kvs_data.append((u'材料', self.material))
        kvs_data.append((u'单位', self.unit))
        return kvs_data

@receiver(post_save, sender=Caigou)
def update_product_type(sender, instance, created, *args, **kwargs):
    if created == True:
        instance.type='CAIGOU'
        instance.save()

class CaigouForm(ModelForm):
    class Meta:
        model = Caigou
        fields = ('name', 'supplier', 'specs', 'material', 'unit')
        labels={
            'name': u'昵称',
            'supplier': u'供应商',
            'specs': u'规格',
            'material': u'材料',
            'unit': u'单位(个/件/米)',
        }


