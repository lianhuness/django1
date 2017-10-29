# coding=utf-8
# author= YQZHU

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.shortcuts import get_object_or_404

from .client_models import Client, ClientForm
from .user_models import Sales

def list_clients(request):
    # clients = request.user.client_set.all()
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'clients/list_clients.html', context)

def my_clients(request):
    # clients = request.user.client_set.all()
    sales = get_object_or_404(Sales, pk=request.user.hdcrmuserinfo.id)
    clients =sales.client_set.all()
    context = {'clients': clients}
    return render(request, 'clients/list_clients.html', context)

def view_client(request, id):
    client = get_object_or_404(Client, pk=id)
    context = {'client': client}
    return render(request, 'clients/view_client.html', context)

def add_client(request):
    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            client = client_form.save(commit=False)
            client = client.save()
            return redirect(reverse('list_clients'))
    else:
        client_form = ClientForm()

    context = {'client_form': client_form}
    return render(request, 'clients/add_client.html', context)

def edit_client(request, id):
    client = get_object_or_404(Client, pk=id)
    if request.method == 'POST':
        client_form = ClientForm(request.POST, instance=client)
        if client_form.is_valid():
            client_form.save()
            return redirect(reverse('view_client', kwargs={'id':client.id}))
    else:
        client_form = ClientForm(instance=client)

    context = {'client': client, 'client_form':client_form}
    return render(request, 'clients/edit_client.html', context)