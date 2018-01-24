# coding=utf-8


from django.conf.urls import url,include
from django.contrib import admin
from permission import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^loginhtml/$", views.loginhtml, name="loginhtml"),
    url(r"^login/$", views.login, name="login"),
    url(r"^addrolepage/$", views.addrolepage, name="addrolepage"),
    url(r"^addrole/$", views.addrole, name="addrole"),
    url(r"^rolelist/$", views.rolelist, name="rolelist"),
    url(r"^resourceadd/$", views.resourceadd, name="resourceadd"),
    # url(r"^resourceselect/$", views.resourceselect, name="resourceselect"),
]