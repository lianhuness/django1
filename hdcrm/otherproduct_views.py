# coding=utf-8
# author= YQZHU

from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from .otherproduct_models import OtherLatex, OtherLatexForm, Pvc, PvcForm, OtherProduct, OtherProductsForm


def add_otherlatex(request):
    if request.method == 'POST':
        form = OtherLatexForm(request.POST)
        if form.is_valid():
            pb=form.save(commit=False)
            pb.user = request.user
            pb.save()
            return redirect(reverse('view_product', kwargs={'id': pb.id}))
    else:
        form = OtherLatexForm()
    context = {'form': form}
    return render(request, 'products/add_otherlatex.html', context)

def add_pvc(request):
    if request.method == 'POST':
        form = PvcForm(request.POST)
        if form.is_valid():
            pb=form.save(commit=False)
            pb.user = request.user
            pb.save()
            return redirect(reverse('view_product', kwargs={'id': pb.id}))
    else:
        form = PvcForm()
    context = {'form': form}
    return render(request, 'products/add_pvc.html', context)

def add_other(request):
    if request.method == 'POST':
        form = OtherProductsForm(request.POST)
        if form.is_valid():
            pb=form.save(commit=False)
            pb.user = request.user
            pb.save()
            return redirect(reverse('view_product', kwargs={'id': pb.id}))
    else:
        form = OtherProductsForm()
    context = {'form': form}
    return render(request, 'products/add_other.html', context)

def edit_otherlatex(request, id):
    pb = get_object_or_404(OtherLatex, pk=id)
    if request.method == 'POST':
        form = OtherLatexForm(request.POST,instance=pb)
        if form.is_valid():
            form.save()
            return redirect(reverse('view_product', kwargs={'id': pb.id}))
    else:
        form = OtherLatexForm(instance=pb)
    pb=get_object_or_404(OtherLatex, pk=id)
    context = {'form': form, 'obj': pb, 'editurl': request.path}
    return render(request, 'products/edit_product.html', context)

def edit_pvc(request, id):
    pb = get_object_or_404(Pvc, pk=id)
    if request.method == 'POST':
        form = PvcForm(request.POST,instance=pb)
        if form.is_valid():
            form.save()
            return redirect(reverse('view_product', kwargs={'id': pb.id}))
    else:
        form = PvcForm(instance=pb)
    pb=get_object_or_404(Pvc, pk=id)
    context = {'form': form, 'obj': pb, 'editurl': request.path}
    return render(request, 'products/edit_product.html', context)

def edit_other(request, id):
    pb = get_object_or_404(OtherProduct, pk=id)
    if request.method == 'POST':
        form = OtherProductsForm(request.POST,instance=pb)
        if form.is_valid():
            form.save()
            return redirect(reverse('view_product', kwargs={'id': pb.id}))
    else:
        form = OtherProductsForm(instance=pb)
    pb=get_object_or_404(OtherProduct, pk=id)
    context = {'form': form, 'obj': pb, 'editurl': request.path}
    return render(request, 'products/edit_product.html', context)
