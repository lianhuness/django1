# coding=utf-8
# author= YQZHU

from django.shortcuts import redirect, reverse, render, get_object_or_404

from .sku_models import SkuGroupForm, SkuGroup, Sku, SkuForm
from django.contrib import messages
def add_skugroup(request):
    if request.method == 'POST':
        form = SkuGroupForm(request.POST)
        if form.is_valid():
            sg = form.save()
            return redirect(reverse('view_skugroup', kwargs={'pk': sg.id}))
    else:
        form = SkuGroupForm()
    context = {'form': form }
    return render(request, 'skus/add_skugroup.html', context)

def view_skugroup(request, pk):
    sg = get_object_or_404(SkuGroup, pk=pk)
    context = {'sg': sg}
    return render(request, 'skus/view_skugroup.html', context)

def edit_skugroup(request, pk):
    sg = get_object_or_404(SkuGroup, pk=pk)
    if request.method == 'POST':
        form = SkuGroupForm(request.POST, instance=sg)
        if form.is_valid():
            sg = form.save()
            return redirect(reverse('view_skugroup', kwargs={'pk': sg.id}))
    else:
        form = SkuGroupForm(instance=sg)
    context = {'form': form, 'sg': sg }
    return render(request, 'skus/edit_skugroup.html', context)


def delete_skugroup(request, pk):
    sg = get_object_or_404(SkuGroup, pk=pk)
    sg.delete()
    messages.success(request, u'%s deleted.'%sg)
    return redirect(reverse('donwoo_home'))


from django.shortcuts import HttpResponse
# SKU
def dw_add_sku(request, sg=None):
    if request.method == 'POST':
        form = SkuForm(request.POST)
        if form.is_valid():
            sg = form.save()
            return redirect(reverse('dw_view_sku', kwargs={'pk': sg.id}))
    else:
        form = SkuForm()
        if sg:
            sg = get_object_or_404(SkuGroup, pk=sg)
            form.fields['skuGroup'].initial = sg

    context = {'form': form }
    return render(request, 'skus/dw_add_sku.html', context)

def view_sku(request, pk):
    sg = get_object_or_404(Sku, pk=pk)
    context = {'sg': sg}
    return render(request, 'skus/dw_view_sku.html', context)

def edit_sku(request, pk):
    sg = get_object_or_404(Sku, pk=pk)
    if request.method == 'POST':
        form = SkuForm(request.POST, instance=sg)
        if form.is_valid():
            sg = form.save()
            return redirect(reverse('dw_view_sku', kwargs={'pk': sg.id}))
    else:
        form = SkuForm(instance=sg)
    context = {'form': form, 'sg': sg }
    return render(request, 'skus/dw_edit_sku.html', context)


def delete_sku(request, pk):
    sg = get_object_or_404(Sku, pk=pk)
    sg.delete()
    messages.success(request, u'%s deleted.'%sg)
    return redirect(reverse('donwoo_home'))

#
# # SKU Image
# from .sku_models import SkuImage, SkuImageForm
#
# def dw_add_skuimage(request, pk):
#     sku = get_object_or_404(Sku, pk=pk)
#
#     if request.method == 'POST':
#         form = SkuImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             si = form.save()
#             print(si)
#         return redirect(reverse('dw_view_sku', kwargs={'pk': sku.id}))
#     else:
#         form = SkuImageForm()
#         form.fields['sku'].initial = sku
#     context={'sku': sku, 'form': form}
#     return render(request, 'skus/dw_add_skuimage.html', context)
#
# def dw_delete_skuimg(request, pk):
#     img = get_object_or_404(SkuImage, pk=pk)
#     img.delete()
#     messages.success(request, u'%s deleted.' % img)
#     return redirect(reverse('dw_view_sku', kwargs={'pk': img.sku.id}))
#
#

# SKU File
from .sku_models import SkuFile, SkuFileForm

def dw_add_skufile(request, pk):
    sku = get_object_or_404(Sku, pk=pk)

    if request.method == 'POST':
        form = SkuFileForm(request.POST, request.FILES)
        if form.is_valid():
            si = form.save(commit=False)
            import os.path
            names = os.path.splitext(si.file.name)

            si.filetype=names[1].upper()[1:]
            si.filename = si.file.name
            f = si.save()
            return redirect(reverse('dw_view_sku', kwargs={'pk': sku.id}))
    else:
        form = SkuFileForm()
        form.fields['sku'].initial = sku
    context={'sku': sku, 'form': form}
    return render(request, 'skus/dw_add_skufile.html', context)

def dw_delete_skufile(request, pk):
    img = get_object_or_404(SkuFile, pk=pk)
    img.delete()
    messages.success(request, u'%s deleted.' % img)
    return redirect(reverse('dw_view_sku', kwargs={'pk': img.sku.id}))

# SKU Quote
from .sku_models import SkuQuote, SkuQuoteForm

def dw_add_skuquote(request, pk):
    sku = get_object_or_404(Sku, pk=pk)

    if request.method == 'POST':
        form = SkuQuoteForm(request.POST, request.FILES)
        if form.is_valid():
            si = form.save()

            return redirect(reverse('dw_view_sku', kwargs={'pk': sku.id}))
    else:
        form = SkuQuoteForm()
        form.fields['sku'].initial = sku
    context={'sku': sku, 'form': form}
    return render(request, 'skus/dw_add_skuquote.html', context)

def dw_delete_skuquote(request, pk):
    img = get_object_or_404(SkuQuote, pk=pk)
    img.delete()
    messages.success(request, u'%s deleted.' % img)
    return redirect(reverse('dw_view_sku', kwargs={'pk': img.sku.id}))