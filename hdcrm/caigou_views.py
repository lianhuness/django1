# coding=utf-8
# author= YQZHU

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect

from .caigou_models import Supplier, SupplierForm, Caigou, CaigouForm

def add_supplier(request):
    if request.method == 'POST':
        sf = SupplierForm(request.POST)
        if sf.is_valid():
            sf.save()
            return redirect(reverse('add_caigou'))
    sf = SupplierForm()

    return render(request, 'products/add_supplier.html', {'sf': sf})

def add_caigou(request):
    if request.method == 'POST':
        form = CaigouForm(request.POST)
        if form.is_valid():
            caigou = form.save(commit=False)
            caigou.user = request.user
            caigou.save()
            return redirect(reverse('view_product', kwargs={'id':caigou.id}))
    else:
        form = CaigouForm()
    context = {'form':form}
    return render(request, 'products/add_caigou.html', context)

def edit(request, id):
    obj = get_object_or_404(Caigou, pk=id)
    if request.method == 'POST':
        form = CaigouForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect(reverse('view_product', kwargs={'id': obj.id}))
    else:
        form = CaigouForm(instance=obj)
    obj=get_object_or_404(Caigou, pk=id)
    context = {'form': form, 'obj': obj}
    return render(request, 'products/edit_caigou.html', context)


# def add(request):
#     if request.method == 'POST':
#         powerband_form = PowerbandForm(request.POST)
#
#         if powerband_form.is_valid():
#             pb=powerband_form.save(commit=False)
#             pb.user = request.user
#             # pb.type = 'POWERBAND208'
#             pb.save()
#             return redirect(reverse('view_product', kwargs={'id': pb.id}))
#     else:
#         powerband_form = PowerbandForm()
#         context = {'powerband_form': powerband_form}
#
#         return render(request, 'products/add_powerband.html', context)
#

#
