# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Corpus
import sys
import os
from subprocess import Popen
import requests

reload(sys)
sys.setdefaultencoding('utf-8')

header_str = u"""# -*- coding: utf-8 -*-
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

"""
model_str = u"""
class p%s(models.Model):
    question = models.CharField(max_length = 500, verbose_name = u"问题")
    answer = models.CharField(max_length = 500, verbose_name = u"答案")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name = u"加入时间", editable = False)
    status = models.CharField(verbose_name = u"学习状态", default = '0', choices = STUDY_STATUS, max_length = 12, editable = False)
    common_status = models.CharField(verbose_name = u"是否常见", default = '0', choices = QUESTION_STATUS, max_length = 12, editable = True)
    node = models.CharField(verbose_name = u"节点ID", default = "", blank = True, max_length = 100, editable = False)
    threshold = models.CharField(verbose_name = u"阈值", default = "0.2", max_length=10, help_text=u"请输入0~1的值。")

    class Meta:
        verbose_name = u"%s"
        verbose_name_plural = u"%s"


class Resource%s(resources.ModelResource):
    class Meta:
        model = p%s
        fields = ('id', 'question', 'answer', 'threshold')
        import_id_fields = ('id', 'question', 'answer', 'threshold')
        export_order = ('id', 'question', 'answer', 'threshold')
PAdmin.resource_class = Resource%s
admin.site.register(p%s, PAdmin)
CLASS_MAP["p%s"] = p%s
"""

def createNewModel():
    # with open("/var/www/eai/src/corpus_list/models.py", 'w') as f:
    with open("/Users/Egglee/eai/corpus_list/models.py", 'w') as f:
        print >> f, header_str
        for obj in Corpus.objects.all():
            try:
                requests.get("http://120.26.132.118:8080/nuoyuan/services/p%s/api?name=%s" % (obj.id, obj.corpus_name))
            except Exception, e:
                pass
            print >> f, (model_str % (obj.id, obj.corpus_name, obj.corpus_name, obj.id, obj.id, obj.id, obj.id,obj.id,obj.id))
    with open('/tmp/1.sh', 'w') as f:
        print >> f, """
cd /Users/Egglee/eai
echo -e "N\\nN\\nN\\nN\\nN\\nN\\nN\\nN\\nN" | python manage.py makemigrations >/tmp/log 2>&1
echo "yes\\nyes\\nyes\\nyes" | python manage.py migrate >>/tmp/log 2>&1
echo -e "N\\nN\\nN\\nN\\nN\\nN\\nN\\nN\\nN" | python manage.py runserver 8080
echo restart | nc localhost 22222 -q 0
"""
    os.system("cd /tmp; chmod a+x /tmp/1.sh; \nnohup bash /tmp/1.sh &")

class CorpusAdmin(admin.ModelAdmin):
    list_display = ('corpus_name', 'id', 'creater', 'create_time', 'memo')
    search_fields = ('corpus_name', 'creater', 'memo')
    list_filter = ('corpus_name', 'creater', 'create_time')
    actions = ['delete_selected']

    def delete_selected(self, request, obj):
        for o in obj.all():
            o.delete()
        createNewModel()
    delete_selected.short_description = u'批量删除'

    def save_model(self, request, obj, form, change):
        super(CorpusAdmin, self).save_model(request, obj, form, change)
        createNewModel()

    def delete_model(self, request, obj):
        super(CorpusAdmin, self).delete_model(request, obj)
        createNewModel()

admin.site.register(Corpus, CorpusAdmin)


