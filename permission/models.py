# coding=utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.

# 用户表
class FyyUsers(models.Model):
    user_name = models.CharField(max_length=255)
    pwd = models.CharField(max_length=255)
    sex = models.IntegerField()
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=255)
    class Meta:
        ordering = ["id"]
        db_table = "fyy_users"

# 用户角色关系表
class FyyUsersRole(models.Model):
    user_id = models.BigIntegerField()
    role_id = models.BigIntegerField()
    create_id = models.BigIntegerField()
    crt_time = models.DateTimeField()
    class Meta:
        ordering = ["id"]
        db_table = "fyy_users_role"

# 角色
class FyyRole(models.Model):
    role = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    enabled = models.BooleanField(default=True)
    create_id = models.BigIntegerField()
    crt_time = models.DateTimeField()
    update_id = models.BigIntegerField()
    update_time = models.DateTimeField()
    remark = models.TextField(max_length=500)
    class Meta:
        ordering = ["id"]
        db_table = "fyy_role"

# 角色权限关系
class FyyRolePermission(models.Model):
    role_id = models.BigIntegerField()
    permission_id = models.BigIntegerField()
    create_id = models.BigIntegerField()
    crt_time = models.DateTimeField()
    class Meta:
        ordering = ["id"]
        db_table = "fyy_role_permission"

# 权限
class FyyPermission(models.Model):
    name = models.BigIntegerField()
    des = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    sort = models.IntegerField()
    p_id = models.BigIntegerField()
    p_ids = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    permission = models.CharField(max_length=255)
    avaliable = models.BooleanField(default=True)
    class Meta:
        ordering = ["id"]
        db_table = "fyy_permission"
