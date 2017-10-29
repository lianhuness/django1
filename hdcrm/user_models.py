# coding=utf-8
# author= YQZHU

from django.contrib.auth.models import User
from django.db import models

USER_TYPE_CHOICE=(
    ('SALES', u'销售员'),
    ('BUYER', u'采购员'),
    ('TONGJI', u'统计员'),
    ('CAOZUOYUAN', u'操作员'),
    ('ADMIN', u'主管'),
)

class HdcrmUserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=USER_TYPE_CHOICE)

    def __str__(self):
        if self.type=='SALES':
            return u"%s - %s"%(self.get_type_display(), Sales.objects.get(pk=self.id).mark)
        return self.get_type_display()

class Sales(HdcrmUserInfo):
    mark = models.CharField(max_length=1, unique=True)

    def clean(self):
        self.mark = self.mark.capitalize()
    def __str__(self):
        return "%s(%s)"%(self.user.first_name, self.mark)

from django import forms
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        label=u"用户名",
        max_length=30,
    )
    password = forms.CharField(
        label=u"密码",
        widget=forms.PasswordInput,
    )


class SignupForm(forms.Form):
    username = forms.CharField(
        label=u"用户名",
        max_length=30,
    )
    first_name=forms.CharField(
        label=u"姓名",
        max_length=100,
    )
    password_1 = forms.CharField(
        label=u"密码",
        widget=forms.PasswordInput,
    )
    password_2 = forms.CharField(
        label=u"确认密码",
        widget=forms.PasswordInput,
    )
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(u'用户已经存在')
        return username
    def clean_password_2(self):
        password_1 = self.cleaned_data.get("password_1")
        password_2 = self.cleaned_data.get("password_2")
        if password_1 and password_2 and password_1 != password_2:
            raise forms.ValidationError(_(u'两次密码不一致'))
        return password_2

class AddSalesForm(SignupForm, forms.ModelForm):
    class Meta:
        model = Sales
        fields = ('mark',)
        labels = {'mark': u'代码'}



