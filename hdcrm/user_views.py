# coding=utf-8
# author= YQZHU

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse

from .user_models import HdcrmUserInfo, Sales, AddSalesForm, LoginForm

def listusers(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users/listusers.html', context)

def login_user(request):
    if request.method=='POST':
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse(u"用户冻结， 联系管理员")
            else:
                return HttpResponse(u"密码错误")
    else:
        login_form=LoginForm()
    context = {'login_form': login_form}
    return render(request, 'users/login_user.html', context)

def logout_user(request):
    logout(request)
    return redirect('/')

def add_sales(request):
    if request.method == 'POST':
        signup_form = AddSalesForm(request.POST)
        if signup_form.is_valid():
            signup_info = signup_form.cleaned_data
            username = signup_info['username']
            first_name = signup_info['first_name']
            password = signup_info['password_1']
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                password=password)
            user.save()
            Sales.objects.create(user=user, type='SALES', mark=signup_info['mark'])

            return redirect(reverse('listusers'))
    else:
        signup_form = AddSalesForm()
    context = {'signup_form': signup_form}
    return render(request, 'users/add_sales.html', context)
