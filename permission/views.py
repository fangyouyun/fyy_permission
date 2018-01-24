# coding=utf-8

from django.shortcuts import render
from django.http import request,response
from models import FyyUsers,FyyRole,FyyPermission
from django.db import models
import time
from django.views.decorators.cache import cache_page

# Create your views here.
@cache_page(60*15)
def index(request):
    return render(request, "permission/index.html")

# 登录
def loginhtml(request):
    return render(request, "permission/login.html", {"errorCode":"login"})

def login(request):
    username = request.POST["username"]
    pwd = request.POST["pwd"]
    print("username:%s,pwd:%s" % (username, pwd))
    context = {"username": username, "pwd": pwd}
    # 校验用户名密码是否在数据库中存在
    count = FyyUsers.objects.filter(user_name=username).filter(pwd=pwd).count()
    if count == 0 : # 说明这个账号或密码有误
        return render(request, "permission/404.html", {"errorCode":"notlogin"})
    else:
        return render(request, "permission/index.html", context)

# 角色添加页面
def addrolepage(request):
    return render(request, "permission/role/roleadd.html")
# 角色添加
def addrole(request):
    role = request.POST["role"]
    description = request.POST["description"]
    enabled = request.POST["enable"]
    remark = request.POST["remark"]
    # 存入到数据库中，拦截当前操作用户
    fyyRole = FyyRole()
    fyyRole.role = role
    fyyRole.description = description
    fyyRole.enabled = enabled
    fyyRole.remark = remark
    fyyRole.save()
    return render(request, "permission/role/roleadd.html")
# 角色列表
def rolelist(request):
    rolelist = FyyRole.objects.all()
    return render(request, "permission/role/rolelist.html", {"rolelist": rolelist})

# 资源页面
def resourceadd(request):
    # 找出所有的资源，并返回
    list = FyyPermission.objects.filter(avaliable=1)
    print(list)
    return render(request, "permission/resource/resourceadd.html", {"list":list})
# select
"""
def resourceselect(request):
    # 找出所有的资源，并返回
    list = FyyPermission.objects.filter(avaliable=1)
    print(list)
    return render(request, "permission/resource/resourceadd.html",{"list":list});
"""