# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from django.contrib import admin
from django.core.validators import RegexValidator
from django.utils.html import escape, mark_safe
import urllib2
from views import host
from views import CLASS_MAP
import json
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class PAdmin(ImportExportModelAdmin):
    list_display = ('id', 'question', 'answer', 'create_time', 'status', 'common_status', 'node','threshold', 'button')
    search_fields = ('id', 'question', 'answer', 'create_time', 'status')
    list_filter = ('id',  'create_time', 'status')
    list_per_page = 15
    actions = ['delete_selected']

    def button(self, obj):
        if obj.status == '0':
            learn_button = '<a href="#" %s class="btn btn-success">学习</a>' % \
('onclick="var str = window.prompt(\'请输入title，默认为问题\', \'%s\'); if (str != \'\') {$.ajax( {url: \'/corpus/api/learn\', data: {\'class\': \'%s\', \'id\': \'%d\', \'question\': str, \'answer\': \'%s\'}, async: true, type: \'get\', dataType: \'json\', success: function (res) { if (res[\'is_success\'] == true) {location.reload();} else {alert(res[\'error\']);} }, error: function(e) {alert(e);} }); }"' % \
(obj.question.replace('\'', '').replace('\"', ''), type(obj).__name__, obj.id, obj.answer.replace('\'', '').replace('\"', '')),)
            assiote_button = ''
        else:
            learn_button = ''
            assiote_button = '<a href="#" %s class="btn btn-success"> 关联 </a>' % \
('onclick="var str = window.prompt(\'请输入需要关联的id或nodeid\');  if (str != \'\') { var value = window.prompt(\'请输入阈值\', \'%s\'); if (value != \'\') { var sents = window.prompt(\'请输入基本句子,多条用||分割.\'); $.ajax( {url: \'/corpus/api/associate\', data: {\'class\': \'%s\', \'id\': \'%d\', \'to\': str, \'threshold\': value, \'question\': str, \'answer\': \'%s\', \'sentences\': sents}, async: true, type: \'get\', dataType: \'json\', success: function (res) { if (res[\'is_success\'] == true) {alert(\'操作成功！\');location.reload();} else {alert(res[\'error\']);} }, error: function(e) {alert(e);} }); } }"' % \
(obj.threshold, type(obj).__name__, obj.id, obj.answer.replace('\'', '').replace('\"', '')),)


            assiote_button = assiote_button + '<a href="#" %s class="btn btn-success"> 添加 </a>' % \
('onclick="var value = window.prompt(\'请输入阈值\', \'%s\'); if (value != \'\') { var sents = window.prompt(\'请输入基本句子,多条用||分割.\'); $.ajax( {url: \'/corpus/api/associate\', data: {\'class\': \'%s\', \'id\': \'\', \'to\': \'%d\', \'threshold\': value, \'answer\': \'%s\', \'sentences\': sents}, async: true, type: \'get\', dataType: \'json\', success: function (res) { if (res[\'is_success\'] == true) { alert(\'操作成功！\');location.reload();} else {alert(res[\'error\']);} }, error: function(e) {alert(e);} }); }"' % \
(obj.threshold, type(obj).__name__, obj.id, obj.answer.replace('\'', '').replace('\"', '')),)

        delete_button = '<a href="/admin/corpus_list/%s/%d/delete/" class="btn btn-danger">删除</a>' % (type(obj).__name__, obj.id)
        return mark_safe('<ul class="object-tools" style="float: left;" >' + \
                learn_button + assiote_button + delete_button + \
                '</ul>')

    button.short_description = u"操作"
    button.allow_tags = True

    def deleteobj(self, obj):
        if len(obj.node) > 1:
            response = urllib2.urlopen("%s/ai/macrossx/%s/delete/%s"                     % (host, type(obj).__name__, obj.node))
            ret_data = json.loads(''.join(response.readlines()))
            if int(ret_data['status']) != 0:
                raise Exception(u'内核返回异常: %s' % (json.dumps(ret_data, ensure_ascii = False), ))

    def delete_selected(self, request, obj):
        for o in obj.all():
            self.deleteobj(o)
            o.delete()
    delete_selected.short_description = u'批量删除'

    def save_model(self, request, obj, form, change):
        super(PAdmin, self).save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        self.deleteobj(obj)
        super(PAdmin, self).delete_model(request, obj)





