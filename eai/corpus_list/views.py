# coding:utf-8
import StringIO

from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.core import serializers
import MySQLdb
from django.template import Template, Context
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template import Context
from django.db.models import Q
from host import host
import os
import corpus
import json
import sys
import urllib
import urllib2
import sys
import datetime, time
import mysql.connector
import xlwt


reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.

ret_json = {
    "is_success": True,
    "value": {},
    "error": "",
}
CLASS_MAP = {}

def toDict(model):
    return dict([(attr, str(getattr(model, attr))) for attr in [f.name for f in model._meta.fields]])

def addQuestion(request):
    ret = ret_json.copy()
    questions = None
    answers = None
    try:
        dbref = request.POST['dbref']
        for i in range(0, 99999):
            if request.POST.has_key('answer[%d]' % (i,)) and request.POST.has_key('question[%d]' % (i,)):
                try:
                    CLASS_MAP[dbref].objects.create(
                        question = request.POST['question[%d]' % (i,)],
                        answer =  request.POST['answer[%d]' % (i,)]
                    )
                except Exception, e:
                    continue
            else:
                break
    except Exception, e:
        ret['is_success'] = False
        ret['error'] = str(e)
    ret['post'] = request.POST
    return HttpResponse(json.dumps(ret, ensure_ascii = False),
            content_type = "application/json")

def getCommonQuestions(request):
    ret = ret_json.copy()
    try:
        ret['value'] = []
        for data in CLASS_MAP[request.GET['dbref']].objects.filter(common_status="1"):
            ret['value'].append(toDict(data))
    except Exception, e:
        ret['is_success'] = False
        ret['error'] = str(e)
    return HttpResponse(json.dumps(ret, ensure_ascii = False),
            content_type = "application/json")


def learn(request):
    ret = ret_json.copy()
    try:
        data = {
            'title': request.GET['question'],
            'answer': request.GET['answer'],
        }
        response = urllib2.urlopen("%s/ai/macrossx/%s/add/node?%s" \
                    % (host, request.GET['class'], urllib.urlencode(data)))
        ret_data = json.loads(''.join(response.readlines()))
        if int(ret_data['status']) != 0:
            raise Exception(u'内核返回异常：ret：%s'% ( \
                    json.dumps(ret_data, ensure_ascii = False), ))
        else:
            objs = CLASS_MAP[request.GET['class']].objects.filter(
                    id = request.GET['id']
                    )
            if objs:
                for obj in objs:
                    obj.status = '1'
                    obj.node = ret_data['result']['id']
                    obj.save()
    except Exception, e:
        ret['is_success'] = False
        ret['error'] = str(e)
    return HttpResponse(json.dumps(ret, ensure_ascii = False),
            content_type = "application/json")

def associate(request):
    ret = ret_json.copy()
    try:
        objs = None
        try:
            fr = int(request.GET['id'])
            objs = CLASS_MAP[request.GET['class']].objects.filter(
                    id = fr
                    )
        except Exception, e:
            fr = request.GET['id']
            pass
        if objs:
            for obj in objs:
                fr = obj.node
        to = int(request.GET['to'])
        objs = CLASS_MAP[request.GET['class']].objects.filter(
               Q(id = to) |
               Q(node = to)
               )
        if objs:
            for obj in objs:
                to = obj.node
        else:
            raise Exception("id: %s not found!" % (to, ))
        data = {
            'from': fr,
            'to': to,
            'threshold': request.GET['threshold'],
            'sentences': request.GET['sentences'],
        }
        response = urllib2.urlopen("%s/ai/macrossx/%s/add/connection?%s" \
                    % (host, request.GET['class'], urllib.urlencode(data)))
        ret_data = json.loads(''.join(response.readlines()))
        if int(ret_data['status']) != 0:
            raise Exception(u'内核返回异常：ret：%s'% ( \
                    json.dumps(ret_data, ensure_ascii = False), ))
    except Exception, e:
        ret['is_success'] = False
        ret['error'] = str(e)
    return HttpResponse(json.dumps(ret, ensure_ascii = False),
            content_type = "application/json")

def getDbs(request):
    ret = ret_json.copy()
    try:
        dbs = corpus.models.Corpus.objects.all()
        ret['value'] = []
        for db in dbs:
            ret['value'].append({
                'dbname': db.corpus_name,
                'dbref': 'p%d' % (db.id,)
            })
        return HttpResponse(json.dumps(ret, ensure_ascii = False),
            content_type = "application/json")
    except Exception, e:
        ret['is_success'] = False
        ret['error'] = str(e)
    return HttpResponse(json.dumps(ret, ensure_ascii = False),
            content_type = "application/json")

def reloadDb(request):
    ret = ret_json.copy()
    try:
        response = urllib2.urlopen("%s/ai/macrossx/%s/reload" \
                    % (host, request.GET['dbref']))
        ret_data = json.loads(''.join(response.readlines()))
        if int(ret_data['status']) != 0:
            raise Exception(u'内核返回异常：ret：%s'% ( \
                    json.dumps(ret_data, ensure_ascii = False), ))
        return HttpResponse(json.dumps(ret, ensure_ascii = False),
            content_type = "application/json")
    except Exception, e:
        ret['is_success'] = False
        ret['error'] = str(e)
    return HttpResponse(json.dumps(ret, ensure_ascii = False),
            content_type = "application/json")

def resetHost(request):
    ret = ret_json.copy()
    try:
        raise Exception('禁止修改内核地址')
        with open("/Users/Egglee/eai/corpus_list/host.py", 'w') as f:
            print >> f, "host = \"%s\"" % (request.GET['host'],)
        os.system("echo restart | nc localhost 22222 -q 0");

    except Exception, e:
        ret['is_success'] = False
        ret['error'] = str(e)
    return HttpResponse(json.dumps(ret, ensure_ascii = False),
            content_type = "application/json")

start_date = None
end_date = None

def dateKPI(request):
    fp = open('/Users/Egglee/eai/templates/exportKPI.html')
    t = Template(fp.read())
    c = Context({
    })
    html = t.render(c)
    global start_date
    global end_date
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    fp.close()
    return HttpResponse(html)



def exportKPI(request):
    global start_date
    global end_date

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s' % 'KPI_{time}.xls'.format(time=time.ctime())

    wb = xlwt.Workbook(encoding='utf-8')
    sheet = wb.add_sheet(u'KPI报表')
    sheet.write(0, 0, '日期')
    sheet.write(0, 1, '共咨询客户数')
    sheet.write(0, 2, '人工响应次数')
    sheet.write(0, 3, '人工平均响应时间')
    sheet.write(0, 4, '机器人回复兜底话术次数')
    info = {
    'host'    :'rds6a1w2l8bn42e9549yo.mysql.rds.aliyuncs.com',
    'user'    :'root01',
    'password':'root01',
    'database':'eai-core'
    }
    conn = mysql.connector.connect(**info)
    cursor1 = conn.cursor()
    cursor2 = conn.cursor()
    start = datetime.date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10]))
    end = datetime.date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10]))

    # sqlstr = 'SELECT COUNT(DISTINCT(fromip) FROM sys_log '
    # sqlstr = 'SELECT COUNT(*) FROM sys_log  WHERE noanswer = 1 AND left(logtime,10) = "%s" ' % start_date
    # for da in range(start, end, datetime.timedelta(days=1)):
    #     sqlstr = 'SELECT COUNT(*) FROM sys_log  WHERE noanswer = 1 AND left(logtime,10) = "%s" ' % da
    #     cursor.execute(sqlstr)
    #     num = [row[0] for row in cursor.fetchall()]
    #     sheet.write(1, 4, num[0])



    d = start
    n = (end-start).days+1
    for i in range(n):
        while d <= end:
            sheet.write(i+1, 0, d.strftime('%Y-%m-%d'))
            sqlstr1 = 'SELECT COUNT(*) FROM sys_log  WHERE noanswer = 1 AND left(logtime,10) = "%s" ' % d.strftime('%Y-%m-%d')
            cursor1.execute(sqlstr1)
            num = [row[0] for row in cursor1.fetchall()]
            sheet.write(i+1, 4, num[0])
            sqlstr2 = 'SELECT COUNT(DISTINCT(fromip)) FROM sys_log WHERE left(logtime,10) = "%s" ' % d.strftime('%Y-%m-%d')
            cursor2.execute(sqlstr2)
            num = [row[0] for row in cursor2.fetchall()]
            sheet.write(i+1, 1, num[0])
            i += 1
            d += datetime.timedelta(days=1)

    output = StringIO.StringIO()
    wb.save(output)
    output.seek(0)
    response.write(output.getvalue())

    return response


