# coding=utf-8
# author= YQZHU

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect

from .powerband_models import Powerband, PowerbandForm


def add(request):
    if request.method == 'POST':
        powerband_form = PowerbandForm(request.POST)

        if powerband_form.is_valid():
            pb=powerband_form.save(commit=False)
            pb.user = request.user
            pb.save()
            return redirect(reverse('view_product', kwargs={'id': pb.id}))
    else:
        powerband_form = PowerbandForm()

    context = {'powerband_form': powerband_form}

    return render(request, 'products/add_powerband.html', context)

def edit(request, id):
    pb = get_object_or_404(Powerband, pk=id)
    print(pb.name)
    if request.method == 'POST':
        pb_form = PowerbandForm(request.POST,instance=pb)
        if pb_form.is_valid():
            pb_form.save()
            return redirect(reverse('view_product', kwargs={'id': pb.id}))
    else:
        pb_form = PowerbandForm(instance=pb)
    pb=get_object_or_404(Powerband, pk=id)
    context = {'pb_form': pb_form, 'pb': pb}
    return render(request, 'products/edit_powerband.html', context)

    return HttpResponse("Edit")


