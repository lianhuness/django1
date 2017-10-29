# coding=utf-8
# author= YQZHU

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect

from .product_models import Product, PRODUCT_CHOICE
from .powerband_models import Powerband
from .caigou_models import Caigou
from .latexband_models import LatexBand
from .otherproduct_models import OtherLatex, OtherProduct, Pvc
from django.views.generic import ListView, DetailView
from django.contrib import messages

from django.db.models import Count

def getTypeDisplay(type):
    for i in PRODUCT_CHOICE:
        if i[0]== type:
            return i[1]
    return "UNKNOWN"

def list_products(request, product_type="ALL"):
    print(product_type)
    if product_type == 'ALL':
        obj_list = Product.objects.all()
    else:
        if getTypeDisplay(product_type) == "UNKNOWN":
            return HttpResponse(u"参数错误")
        else:
            obj_list = Product.objects.filter(type=product_type)

    tcObjs = Product.objects.values('type').annotate(Count('id')).order_by('-id__count')

    typeCounts = []

    typeCounts.append({'type_display': u'所有产品',
                       'id__count': Product.objects.all().count(),
                       'type': 'ALL',
                       'is_active': '',
                       })
    if product_type=='ALL':
        typeCounts[0]['is_active']='active'

    for tc in tcObjs:
        if tc['type'] == product_type:
            is_active='active'
        else:
            is_active=""

        typeCounts.append({'type_display': getTypeDisplay(tc['type']),
                           'id__count': tc['id__count'],
                           'type': tc['type'],
                            'is_active': is_active,
                           })
    context = {'object_list': obj_list, 'typeCounts': typeCounts, 'product_type': product_type}
    return render(request, 'products/list_products.html', context)

def view_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.type == 'POWERBAND208':
        product = get_object_or_404(Powerband, pk=id)
    elif product.type == 'CAIGOU':
        product = get_object_or_404(Caigou, pk=id)
    elif product.type == 'LATEXBAND':
        product = get_object_or_404(LatexBand, pk=id)
    elif product.type == 'OTHERLATEX':
        product = get_object_or_404(OtherLatex, pk=id)
    elif product.type == 'PVC':
        product = get_object_or_404(Pvc, pk=id)
    elif product.type == 'OTHERS':
        product = get_object_or_404(OtherProduct, pk=id)

    context = {'product': product}

    return render(request, 'products/view_product.html', context)


def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.type == 'POWERBAND208':
        return redirect(reverse('edit_powerband', kwargs={'id': id}))
    elif product.type == 'CAIGOU':
        return redirect(reverse('edit_caigou', kwargs={'id':id}))
    elif product.type == 'LATEXBAND':
        return redirect(reverse('edit_latexband', kwargs={'id':id}))
    elif product.type == 'OTHERLATEX':
        return redirect(reverse('edit_otherlatex', kwargs={'id':id}))
    elif product.type == 'PVC':
        return redirect(reverse('edit_pvc', kwargs={'id':id}))
    elif product.type == 'OTHERS':
        return redirect(reverse('edit_other', kwargs={'id':id}))

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.skuitem_set.exists():
        return HttpResponse(u'次产品已经使用在 SKU 里, 不能删除！')
    product.delete()
    messages.add_message(request, messages.SUCCESS, u'产品已经删除 %s'%product)

    redirect_to = request.GET.get('next', '')
    if redirect_to:
        return redirect(redirect_to)
    return redirect(reverse('list_products'))