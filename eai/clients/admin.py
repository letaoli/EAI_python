from django.contrib import admin
from models import Clients
import sys
import os
from subprocess import Popen
import requests

reload(sys)
sys.setdefaultencoding('utf-8')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'email', 'company', 'position')
    search_field = ('name', 'mobile', 'email', 'company', 'position')

admin.site.register(Clients, ClientAdmin)
