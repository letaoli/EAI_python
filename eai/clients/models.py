# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class Clients(models.Model):
    name = models.CharField(max_length = 100, verbose_name = u"姓名", unique = True)
    mobile = models.CharField(max_length = 11, verbose_name = u"手机")
    email = models.CharField(max_length = 30, verbose_name = u"邮箱")
    company = models.CharField(max_length = 30, verbose_name = u"公司")
    position = models.CharField(max_length = 30, verbose_name = u"职位")

    class Meta:
        verbose_name = u"客户管理"
        verbose_name_plural = u"客户管理"
