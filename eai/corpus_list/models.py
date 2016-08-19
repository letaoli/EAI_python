# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.core.validators import RegexValidator
from django.utils.html import escape, mark_safe
import urllib2
from views import host
from views import CLASS_MAP
from admin import PAdmin
import json
from import_export import resources
from import_export.admin import ImportExportModelAdmin


STUDY_STATUS = (
        ('0', '待学习'),
        ('1', '已学习'),
        )

QUESTION_STATUS = (
        ('0', '非常见问题'),
        ('1', '常见问题'),
        )



class p1(models.Model):
    question = models.CharField(max_length = 500, verbose_name = u"问题")
    answer = models.CharField(max_length = 500, verbose_name = u"答案")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name = u"加入时间", editable = False)
    status = models.CharField(verbose_name = u"学习状态", default = '0', choices = STUDY_STATUS, max_length = 12, editable = False)
    common_status = models.CharField(verbose_name = u"是否常见", default = '0', choices = QUESTION_STATUS, max_length = 12, editable = True)
    node = models.CharField(verbose_name = u"节点ID", default = "", blank = True, max_length = 100, editable = False)
    threshold = models.CharField(verbose_name = u"阈值", default = "0.2", max_length=10, help_text=u"请输入0~1的值。")

    class Meta:
        verbose_name = u"万达"
        verbose_name_plural = u"万达"


class Resource1(resources.ModelResource):
    class Meta:
        model = p1
        fields = ('id', 'question', 'answer', 'threshold')
        import_id_fields = ('id', 'question', 'answer', 'threshold')
        export_order = ('id', 'question', 'answer', 'threshold')
#PAdmin.resource_class = Resource1
admin.site.register(p1, PAdmin)
CLASS_MAP["p1"] = p1


class p6(models.Model):
    question = models.CharField(max_length = 500, verbose_name = u"问题")
    answer = models.CharField(max_length = 500, verbose_name = u"答案")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name = u"加入时间", editable = False)
    status = models.CharField(verbose_name = u"学习状态", default = '0', choices = STUDY_STATUS, max_length = 12, editable = False)
    common_status = models.CharField(verbose_name = u"是否常见", default = '0', choices = QUESTION_STATUS, max_length = 12, editable = True)
    node = models.CharField(verbose_name = u"节点ID", default = "", blank = True, max_length = 100, editable = False)
    threshold = models.CharField(verbose_name = u"阈值", default = "0.2", max_length=10, help_text=u"请输入0~1的值。")

    class Meta:
        verbose_name = u"测试1"
        verbose_name_plural = u"测试1"


class Resource6(resources.ModelResource):
    class Meta:
        model = p6
        fields = ('id', 'question', 'answer', 'threshold')
        import_id_fields = ('id', 'question', 'answer', 'threshold')
        export_order = ('id', 'question', 'answer', 'threshold')
#PAdmin.resource_class = Resource6
admin.site.register(p6, PAdmin)
CLASS_MAP["p6"] = p6


class p8(models.Model):
    question = models.CharField(max_length = 500, verbose_name = u"问题")
    answer = models.CharField(max_length = 500, verbose_name = u"答案")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name = u"加入时间", editable = False)
    status = models.CharField(verbose_name = u"学习状态", default = '0', choices = STUDY_STATUS, max_length = 12, editable = False)
    common_status = models.CharField(verbose_name = u"是否常见", default = '0', choices = QUESTION_STATUS, max_length = 12, editable = True)
    node = models.CharField(verbose_name = u"节点ID", default = "", blank = True, max_length = 100, editable = False)
    threshold = models.CharField(verbose_name = u"阈值", default = "0.2", max_length=10, help_text=u"请输入0~1的值。")

    class Meta:
        verbose_name = u"测试3"
        verbose_name_plural = u"测试3"


class Resource8(resources.ModelResource):
    class Meta:
        model = p8
        fields = ('id', 'question', 'answer', 'threshold')
        import_id_fields = ('id', 'question', 'answer', 'threshold')
        export_order = ('id', 'question', 'answer', 'threshold')
#PAdmin.resource_class = Resource8
admin.site.register(p8, PAdmin)
CLASS_MAP["p8"] = p8


class p9(models.Model):
    question = models.CharField(max_length = 500, verbose_name = u"问题")
    answer = models.CharField(max_length = 500, verbose_name = u"答案")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name = u"加入时间", editable = False)
    status = models.CharField(verbose_name = u"学习状态", default = '0', choices = STUDY_STATUS, max_length = 12, editable = False)
    common_status = models.CharField(verbose_name = u"是否常见", default = '0', choices = QUESTION_STATUS, max_length = 12, editable = True)
    node = models.CharField(verbose_name = u"节点ID", default = "", blank = True, max_length = 100, editable = False)
    threshold = models.CharField(verbose_name = u"阈值", default = "0.2", max_length=10, help_text=u"请输入0~1的值。")

    class Meta:
        verbose_name = u"测试4"
        verbose_name_plural = u"测试4"


class Resource9(resources.ModelResource):
    class Meta:
        model = p9
        fields = ('id', 'question', 'answer', 'threshold')
        import_id_fields = ('id', 'question', 'answer', 'threshold')
        export_order = ('id', 'question', 'answer', 'threshold')
#PAdmin.resource_class = Resource9
admin.site.register(p9, PAdmin)
CLASS_MAP["p9"] = p9

