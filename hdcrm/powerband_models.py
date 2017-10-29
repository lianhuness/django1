# coding=utf-8
# author= YQZHU

from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django import forms
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .product_models import  Product, COLOR_CHOICE


class Powerband(Product):
    width = models.DecimalField(max_digits=10, decimal_places=2)
    thickness = models.DecimalField(max_digits=10, decimal_places=2)
    phantom = models.CharField(max_length=20)
    color = models.CharField(max_length=20, choices=COLOR_CHOICE)

    def kvs(self):
        kvs_data=[]
        kvs_data.append((u'宽度(cm)', self.width))
        kvs_data.append((u'厚度(m)', self.thickness))
        kvs_data.append((u'重量(g)', self.weight))
        kvs_data.append((u'潘通色卡号', self.phantom))
        kvs_data.append((u'色系', self.get_color_display()))
        return kvs_data

@receiver(pre_save, sender=Powerband)
def update_powerband_weight(sender, instance, *args, **kwargs):
    instance.weight=round(208*instance.width*instance.thickness/10)

@receiver(post_save, sender=Powerband)
def update_powerband_type(sender, instance, created, *args, **kwargs):
    if created == True:
        instance.type='POWERBAND208'
        instance.save()


class PowerbandForm(ModelForm):
    class Meta:
        model = Powerband
        fields = ('name', 'width', 'thickness', 'phantom', 'color')
        labels={
            'name': u'昵称',
            'width': u'宽度(cm)',
            'thickness': u'厚度(mm)',
            'phantom': u'潘同色号',
            'color': u'色系',
        }
    def clean_phantom(self):
        phantom = self.cleaned_data['phantom']
        width = self.cleaned_data['width']
        thickness = self.cleaned_data['thickness']

        ext = Powerband.objects.filter(phantom=phantom, width=width, thickness=thickness)
        import pdb
        pdb.set_trace()
        if ext.exists():
            raise forms.ValidationError(u'这个颜色和尺寸已经存在： %s'%ext.first())
        return phantom

