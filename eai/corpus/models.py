# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Corpus(models.Model):
    corpus_name = models.CharField(max_length = 100, verbose_name = u"标题", unique = True)
    creater = models.CharField(max_length = 100, verbose_name = u"创建人")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name = u"创建时间", editable = False)
    memo = models.CharField(max_length = 100, verbose_name = u"备注")

    class Meta:
        verbose_name = u"项目管理"
        verbose_name_plural = u"项目管理"
