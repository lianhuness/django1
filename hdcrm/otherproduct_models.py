# coding=utf-8
# author= YQZHU

from django.db import models
from django.forms import ModelForm
from django import forms
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .product_models import  Product, COLOR_CHOICE


class OtherLatex(Product):
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    # weight, note
    def kvs(self):
        kvs_data=[]
        kvs_data.append((u'颜色', product.color))
        kvs_data.append((u'尺寸', product.size))
        kvs_data.append((u'重量(g)', product.weight))
        kvs_data.append((u'附注', product.note))
        return kvs_data

class Pvc(Product):
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    # weight, note
    def kvs(self):
        kvs_data=[]
        kvs_data.append((u'颜色', self.color))
        kvs_data.append((u'尺寸', self.size))
        kvs_data.append((u'重量(g)', self.weight))
        kvs_data.append((u'材料', self.material))
        kvs_data.append((u'附注', self.note))
        return kvs_data

class OtherProduct(Product):
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    # weight, note

    def kvs(self):
        kvs_data=[]
        kvs_data.append((u'颜色', self.color))
        kvs_data.append((u'尺寸', self.size))
        kvs_data.append((u'重量(g)', self.weight))
        kvs_data.append((u'附注', self.note))
        return kvs_data

# @receiver(pre_save, sender=OtherLatex)
# def update_type(sender, instance, *args, **kwargs):
#     instance.weight=round(instance.len*instance.thickness/10*instance.width)

@receiver(post_save, sender=OtherLatex)
def updateType_latex(sender, instance, created, *args, **kwargs):
    if created == True:
        instance.type='OTHERLATEX'
        instance.save()
@receiver(post_save, sender=Pvc)
def updateType_pvc(sender, instance, created, *args, **kwargs):
    if created == True:
        instance.type='PVC'
        instance.save()
@receiver(post_save, sender=OtherProduct)
def updateType_others(sender, instance, created, *args, **kwargs):
    if created == True:
        instance.type='OTHERS'
        instance.save()


class OtherLatexForm(ModelForm):
    class Meta:
        model = OtherLatex
        fields = ('name', 'color', 'size', 'weight', 'note')
        labels={'name': u'昵称', 'color': u'颜色', 'size': u'尺寸', 'weight': u'克重(g)', 'note': u'附注'}

class PvcForm(ModelForm):
    class Meta:
        model = Pvc
        fields = ('name', 'color', 'size', 'weight', 'material',  'note')
        labels={'name': u'昵称', 'color': u'颜色', 'size': u'尺寸', 'weight': u'克重(g)',  'material': u'材料', 'note': u'附注'}
class OtherProductsForm(ModelForm):
    class Meta:
        model = OtherProduct
        fields = ('name', 'color', 'size', 'weight', 'note')
        labels={'name': u'昵称', 'color': u'颜色', 'size': u'尺寸', 'weight': u'克重(g)', 'note': u'附注'}

