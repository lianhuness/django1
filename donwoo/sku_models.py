# coding=utf-8
# author= YQZHU

from django.db import models
IMAGETYPE_LIST=['JPG', 'PNG', "GIF"]

class SkuGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Sku(models.Model):
    skuGroup = models.ForeignKey(SkuGroup)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    created_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

    def imagesTop3(self):
       return self.skufile_set.filter(filetype__in=IMAGETYPE_LIST)[:3]

    def fileCounts(self):
        from django.db.models import Count
        return self.skufile_set.values('filetype').annotate(Count('filetype'))


class Supplier(models.Model):
    companyName = models.CharField(max_length=100)


class SkuSupplier(models.Model):
    sku = models.ForeignKey(Sku)
    supplier = models.ForeignKey(Supplier)
    note = models.TextField()

    def __str__(self):
        return "%s - %s"%(self.sku, self.supplier)

from hongda.settings import MEDIA_ROOT

def sku_upload_to(instance, filename):
    directory =  '/'.join([ 'donwoo', 'sku', instance.sku.skuGroup.name, instance.sku.name, filename])
    print("\n\n\n\n ******************* \n\n\n\n")
    print(directory)
    return directory

# class SkuImage(models.Model):
#     sku = models.ForeignKey(Sku)
#     note = models.TextField(max_length=100)
#     image = models.ImageField(upload_to=sku_upload_to)
#     created_date = models.DateField(auto_now_add=True)
#
#     def __str__(self):
#         return self.note

class SkuFile(models.Model):
    sku = models.ForeignKey(Sku)
    note = models.TextField(max_length=100)
    file = models.FileField(upload_to=sku_upload_to)
    filetype=models.CharField(max_length=20, default='')
    filename = models.CharField(max_length=100, default='####')
    created_date = models.DateField(auto_now_add=True)

    def isImage(self):
        return self.filetype in IMAGETYPE_LIST

    def __str__(self):
        return self.note

from django import forms
class SkuGroupForm(forms.ModelForm):
    class Meta:
        model = SkuGroup
        fields=('name',)

class SkuForm(forms.ModelForm):
    class Meta:
        model = Sku
        fields=('skuGroup', 'name', 'description')
        labels={
            'skuGroup': u'产品类别',
            'name': u'产品名称',
            'description': u'描述',
        }

class SkuFileForm(forms.ModelForm):
    class Meta:
        model = SkuFile
        fields=('sku', 'note', 'file')
        labels={
            'sku': u'产品',
            'note': u'文件说明',
            'file': u'文件',
        }

class SkuQuote(models.Model):
    sku = models.ForeignKey(Sku)
    specs = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s-%s :%s "%(self.sku, self.specs, self.price)

class SkuQuoteForm(forms.ModelForm):
    class Meta:
        model = SkuQuote
        fields=('sku', 'specs', 'price')
