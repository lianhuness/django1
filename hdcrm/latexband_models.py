# coding=utf-8
# author= YQZHU

from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django import forms
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .product_models import  Product, COLOR_CHOICE

ROUND_CHOICE=(
    ('ZHIJIAO', u'直角'),
    ('YUANJIAO', u'圆角'),
)

class LatexBand(Product):
    len = models.DecimalField(max_digits=10, decimal_places=2, default=150)
    width = models.DecimalField(max_digits=10, decimal_places=2, default=15)
    thickness = models.DecimalField(max_digits=10, decimal_places=2)
    phantom = models.CharField(max_length=20)
    color = models.CharField(max_length=20, choices=COLOR_CHOICE)
    round = models.CharField(max_length=10, choices=ROUND_CHOICE, default='ZHIJIAO')

    def kvs(self):
        kvs_data=[]
        kvs_data.append((u'长度(cm)', self.len))
        kvs_data.append((u'宽度(cm)', self.width))
        kvs_data.append((u'厚度(m)', self.thickness))
        kvs_data.append((u'边角切割', self.get_round_display()))
        kvs_data.append((u'重量(g)', self.weight))
        kvs_data.append((u'潘通色卡号', self.phantom))
        kvs_data.append((u'色系', self.get_color_display()))
        return kvs_data

@receiver(pre_save, sender=LatexBand)
def update_latexband_weight(sender, instance, *args, **kwargs):
    instance.weight=round(instance.len*instance.thickness/10*instance.width)

@receiver(post_save, sender=LatexBand)
def update_latexband_type(sender, instance, created, *args, **kwargs):
    if created == True:
        instance.type='LATEXBAND'
        instance.save()


class LatexbandForm(ModelForm):
    class Meta:
        model = LatexBand
        fields = ('name', 'len', 'width', 'thickness', 'round', 'phantom', 'color')
        labels={
            'name': u'昵称',
            'len': u'长度(cm)',
            'width': u'宽度(cm)',
            'thickness': u'厚度(mm)',
            'round': u'边角切割',
            'phantom': u'潘同色号',
            'color': u'色系',
        }

    def clean_phantom(self):
        length = self.cleaned_data['len']
        phantom = self.cleaned_data['phantom']
        width = self.cleaned_data['width']
        thickness = self.cleaned_data['thickness']

        if len(self.changed_data) == 0:
            return phantom
        if len(self.changed_data) == 1 and self.changed_data[0] == 'name':
            return phantom

        ext = LatexBand.objects.filter(len=length, phantom=phantom, width=width, thickness=thickness)

        if ext.exists():
            raise forms.ValidationError(u'这个颜色和尺寸已经存在： %s'%ext.first())
        return phantom

