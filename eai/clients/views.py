# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from models import Clients

# Create your views here.

def index(request):
    if request.method == 'POST':
        Clients.objects.create(
            name = request.POST['name'],
            mobile = request.POST['phone'],
            email = request.POST['email'],
            company = request.POST['company'],
            position = request.POST['position']
        )
        return HttpResponse('<h1>感谢您的注册，请等待客户审核材料后发送邮件到您邮箱~</h1>')
    t = get_template('clients_index.html')
    html = t.render()
    return HttpResponse(html)
