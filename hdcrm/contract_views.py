# coding=utf-8
# author= YQZHU

from django.shortcuts import render, redirect, get_object_or_404, reverse
from .contract_models import Contract, ContractForm, ContractSku,ContractSkuForm
from .client_models import Client

def list_contracts(request):
    contracts = Contract.objects.all()
    context = {'contract_list':contracts}
    return render(request, 'contracts/list_contracts.html', context)

def my_contracts(request):
    context = {'contract_list': request.user.contract_set.all()}
    return render(request, 'contracts/list_contracts.html', context)

def view_contract(request, id):
    contract = get_object_or_404(Contract, pk=id)
    context = {'contract': contract}
    return render(request, 'contracts/view_contract.html', context)

def add_contract(request, cid):
    client = get_object_or_404(Client, pk=cid)
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            contract = form.save()
            return redirect(reverse('view_contract', kwargs={'id': contract.pk} ))
    else:
        form = ContractForm()
        form.fields['sales'].initial = client.sales
        form.fields['client'].initial = client
    context = {'client': client , 'form': form}
    return render(request, 'contracts/add_contract.html', context)

def edit_contract(request, id):
    contract = get_object_or_404(Contract, pk=id)

    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES, instance=contract)
        if form.is_valid():
            contract = form.save()
            return redirect(reverse('view_contract', kwargs={'id': contract.pk} ))
    else:
        form = ContractForm(instance=contract)
    context = {'contract': contract, 'form': form}
    return render(request, 'contracts/edit_contract.html', context)

from .sku_models import Sku
def add_contractsku(request, id):
    contract = get_object_or_404(Contract, pk=id)
    client = contract.client
    hongda = Client.objects.get(name=u'宏大')

    if request.method == 'POST':
        form = ContractSkuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('view_contract', kwargs={'id': contract.pk} ))
    else:
        form = ContractSkuForm()
        form.fields['contract'].initial = contract
        form.fields['sku'].queryset = Sku.objects.filter(client__in=[client, hongda]).all()

    context = {'contract': contract, 'form': form}
    return render(request, 'contracts/add_contractsku.html', context)

def delete_contractsku(request, id):
    cs = get_object_or_404(ContractSku, pk=id)
    cs.delete()
    return redirect(reverse("view_contract", kwargs={'id': cs.contract.id}))

from .contract_models import ContractIncome, ContractIncomeForm

def add_income(request, cid):
    contract = get_object_or_404(Contract, pk=cid)
    if request.method == 'POST':
        form = ContractIncomeForm(request.POST)
        if form.is_valid():
            ci = form.save()
            return redirect(reverse("view_contract", kwargs={'id': contract.id}))
    else:
        form = ContractIncomeForm()
        form.fields['contract'].initial = contract

    context = {'contract': contract, 'form': form}
    return render(request, 'contracts/add_income.html', context)

def view_incomes(request, cid):
    contract = get_object_or_404(Contract, pk=cid)
    context = {'contract': contract }
    return render(request, 'contracts/view_incomes.html', context)

def delete_income(request, id):
    ci = get_object_or_404(ContractIncome, pk=id)
    ci.delete()
    return redirect(reverse("view_contract", kwargs={'id': ci.contract.id}))

from .contract_models import ContractExpense, ContractExpenseForm
def add_expense(request, cid):
    contract = get_object_or_404(Contract, pk=cid)
    if request.method == 'POST':
        form = ContractExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            ci = form.save()
            return redirect(reverse("view_contract", kwargs={'id': contract.id}))
    else:
        form = ContractExpenseForm()
        form.fields['contract'].initial = contract

    context = {'contract': contract, 'form': form}
    return render(request, 'contracts/add_expense.html', context)

def view_expenses(request, cid):
    contract = get_object_or_404(Contract, pk=cid)
    context = {'contract': contract }
    return render(request, 'contracts/view_expenses.html', context)

def delete_expense(request, id):
    ci = get_object_or_404(ContractExpense, pk=id)
    ci.delete()
    return redirect(reverse("view_contract", kwargs={'id': ci.contract.id}))