# coding=utf-8
# author= YQZHU

import os
import sys
import django

pathname = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, pathname)
sys.path.insert(0, os.path.abspath(os.path.join(pathname, '..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hongda.settings")

django.setup()

from hdcrm.client_models import Client
from hdcrm.product_models import Product
from hdcrm.caigou_models import Caigou, Supplier
from hdcrm.powerband_models import Powerband
from django.contrib.auth.models import User
from django.db.models import Q
from hdcrm.user_models import HdcrmUserInfo, Sales

print("Delete user except admin")
print(User.objects.filter(~Q(username='admin')).all())
User.objects.filter(~Q(username='admin')).all().delete()
print("Delete user done. \n\n\n")

print("Delete all Clients")
Client.objects.all().delete()
print("Client data deleted. \n\n\n")

print("Delete all products")
Product.objects.all().delete()
print("Products deleted. \n\n")

print("Delete Suppliers")
Supplier.objects.all().delete()
print("Supplier deleted. \n\n")

print("Client#： %s,  Product#: %s "%(Client.objects.all().count(), Product.objects.all().count()))

print("Create user: User1")

user1 = User.objects.create_user(
                username='caozuoyuan',
                first_name=u'操作员',
                password='Hdjy12345')

HdcrmUserInfo.objects.create(user=user1, type='CAOZUOYUAN')


sales1 = User.objects.create_user(
                username='sales1',
                first_name=u'模拟销售',
                password='12345')
sales1 = Sales.objects.create(user = sales1, type='SALES', mark='T')

sales1.client_set.create(name='Wodfitters', country='USA', district='USA')
sales1.client_set.create(name='Starwoodsport', country='USA', district='USA')
sales1.client_set.create(name=u'铁人体育', country=u'中国', district=u'南通')

# 添加厚圈
Powerband.objects.create(user=user1, name=u'常规红1', width=1.2, thickness=4.5, phantom='XXX', color='RED')
Powerband.objects.create(user=user1, name=u'常规黑1', width=2.2, thickness=4.5, phantom='XXX', color='BLACK')
Powerband.objects.create(user=user1, name=u'常规紫1', width=2.85, thickness=4.5, phantom='XXX', color='PURPLE')

Powerband.objects.create(user=user1, name=u'迪卡侬15KG', width=1.2, thickness=4.5, phantom='XXX', color='RED')
Powerband.objects.create(user=user1, name=u'迪卡侬25KG', width=2.2, thickness=4.5, phantom='XXX', color='BLACK')
Powerband.objects.create(user=user1, name=u'迪卡侬35', width=2.85, thickness=4.5, phantom='XXX', color='PURPLE')


caigouyuan = User.objects.create_user(
                username='caigou1',
                first_name=u'采购员1',
                password='abc')
# 添加供应商
sp_carton = Supplier.objects.create(name='纸箱供应商')
sp_box = Supplier.objects.create(name='彩盒供应商')
sp_bag = Supplier.objects.create(name='PE袋供应商')

Caigou.objects.create(user=caigouyuan, name=u'常规外箱', supplier=sp_carton, specs='42cm*23cm*23cm', material=u'3层瓦楞纸', unit=u'个')
Caigou.objects.create(user=caigouyuan, name=u'Starwoods彩盒1.2cm',supplier=sp_carton, specs='10cm*5cm*5cm', material=u'100g纸', unit=u'个')
Caigou.objects.create(user=caigouyuan, name=u'常规OPP自粘袋',supplier=sp_bag, specs='20cm*10cm', material=u'OPP', unit=u'个')

