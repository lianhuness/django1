# coding=utf-8
# author= YQZHU

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect

from .latexband_models import LatexBand, LatexbandForm


def add(request):
    if request.method == 'POST':
        form = LatexbandForm(request.POST)
        if form.is_valid():
            pb=form.save(commit=False)
            pb.user = request.user
            pb.save()
            return redirect(reverse('view_product', kwargs={'id': pb.id}))
    else:
        form = LatexbandForm()
    context = {'form': form}
    return render(request, 'products/add_latexband.html', context)

def edit(request, id):
    pb = get_object_or_404(LatexBand, pk=id)
    print(pb.name)
    if request.method == 'POST':
        form = LatexbandForm(request.POST,instance=pb)
        if form.is_valid():
            form.save()
            return redirect(reverse('view_product', kwargs={'id': pb.id}))
    else:
        form = LatexbandForm(instance=pb)
    pb=get_object_or_404(LatexBand, pk=id)
    context = {'form': form, 'obj': pb}
    return render(request, 'products/edit_latexband.html', context)

    return HttpResponse("Edit")


