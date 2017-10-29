# coding=utf-8
# author= YQZHU


from django.shortcuts import redirect, render, get_object_or_404, HttpResponse
from .sku_models import SkuGroup

def index(request):
    skugroups = SkuGroup.objects.all()

    context = {'skugroups': skugroups}
    return render(request, 'donwoo/index.html', context)

from django import forms

class SearchForm(forms.Form):
    text = forms.CharField(max_length=100)


def search(request, search_type):
    objs=[]
    if request.method == "POST":
        searchForm = SearchForm(request.POST)
        if searchForm.is_valid():
            from .sku_models import Sku
            objs = Sku.objects.filter(name__icontains=searchForm.cleaned_data['text'])
    else:
        searchForm = SearchForm()

    context = {'search_type': search_type, 'form': searchForm, 'objs': objs}
    return render(request, 'donwoo/donwoo_search.html', context)



