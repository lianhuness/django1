# coding=utf-8
# author= YQZHU

from django.contrib.auth.models import User
from django.db import models

PRODUCT_CHOICE=(
 ('POWERBAND208', u'208圈'),
 ('POWERBAND101', u'101圈'),
 ('5060MINIBAND', u'50/60cm小圈'),
 ('CAIGOU', u'外购件'),
 ('LATEXBAND', u'乳胶片'),
 ('OTHERLATEX', u'其他乳胶制品'),
 ('OTHERS', u'其他产品'),
 ('PVC', u'PVC类'),
)

COLOR_CHOICE=(
    ('RED', u'红'),('ORANGE', u'橙'),('YELLOW', u'黄'),('GREEN', u'绿'),('BLUE', u'蓝'),('BLACK', u'黑'),
    ('PURPLE', u'紫'),('PINK', u'粉'),('NOCOLOR', u'本色'),
)

class Product(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(unique=True, max_length=100, blank=True, default='')
    type = models.CharField(max_length=100, choices=PRODUCT_CHOICE)
    weight = models.PositiveIntegerField(default=0)
    note = models.TextField(null=True, blank=True)

    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s"%(self.get_type_display(), self.name)


    def getProduct(self):
        if self.type == 'POWERBAND208':
            from .powerband_models import Powerband
            return Powerband.objects.get(pk=self.id)
        elif self.type == 'CAIGOU':
            from .caigou_models import Caigou
            return Caigou.objects.get(pk=self.id)
        elif self.type == 'LATEXBAND':
            from .latexband_models import LatexBand
            return LatexBand.objects.get(pk=self.id)
        elif self.type == 'OTHERLATEX':
            from .otherproduct_models import OtherLatex
            return OtherLatex.objects.get(pk=self.id)
        elif self.type == 'PVC':
            from .otherproduct_models import Pvc
            return Pvc.objects.get(pk=self.id)
        elif self.type == 'OTHERS':
            from .otherproduct_models import OtherProduct
            return OtherProduct.objects.get(pk=self.id)
        return self
    

## TEST
class Cost(models.Model):
    product = models.ForeignKey(Product)
    cost = models.PositiveIntegerField()

