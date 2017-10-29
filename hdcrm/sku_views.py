# coding=utf-8
# author= YQZHU

from django.shortcuts import get_object_or_404, render, redirect,reverse
from django.contrib.auth.models import User
from .sku_models import Sku, SkuForm, SkuItem, SkuItemForm
from .client_models import Client


def list_skus(request):
    skus = Sku.objects.all()
    return render(request, 'skus/list_skus.html', {'skus': skus})

def view_sku(request, id):
    sku = get_object_or_404(Sku, pk=id)
    return render(request, 'skus/view_sku.html', {'sku':sku})

def add_sku(request, cid):
    client=get_object_or_404(Client, pk=cid)

    if request.method == 'POST':
        form = SkuForm(request.POST)
        if form.is_valid():
            sku = form.save()
            return redirect(reverse('add_skuitem', kwargs={'sid':sku.pk}))
    else:
        form = SkuForm()
        form.fields['client'].initial=client
        form.fields['user'].initial = request.user

    context = {'form': form, 'client': client}
    return render(request, 'skus/add_sku.html', context)

def edit_sku(request, id):
    sku = get_object_or_404(Sku, pk=id)

    if request.method == 'POST':
        form = SkuForm(request.POST, instance=sku)
        if form.is_valid():
            form.save()
            return redirect(reverse('view_sku', kwargs={'id': sku.id}))
    else:
        form = SkuForm(instance=sku)
    context = {'form': form, 'sku': sku}
    return render(request, 'skus/edit_sku.html', context)


def add_skuitem(request, sid):
    sku = get_object_or_404(Sku, pk=sid)

    if request.method == 'POST':
        form = SkuItemForm(request.POST)
        if form.is_valid():
            skuitem = form.save()
            return redirect(reverse('view_sku', kwargs={'id': sku.id}))
    else:
        form = SkuItemForm()
        form.fields['sku'].initial = sku
    context = {'form': form, 'sku': sku}
    return render(request, 'skus/add_skuitem.html', context)

def del_skuitem(request, id):
    si = get_object_or_404(SkuItem, pk=id)
    si.delete()
    return redirect(reverse('view_sku', kwargs={'id': si.sku.id}))