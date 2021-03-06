# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 04:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='p1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='\u95ee\u9898')),
                ('answer', models.CharField(max_length=500, verbose_name='\u7b54\u6848')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u52a0\u5165\u65f6\u95f4')),
                ('status', models.CharField(choices=[(b'0', b'\xe5\xbe\x85\xe5\xad\xa6\xe4\xb9\xa0'), (b'1', b'\xe5\xb7\xb2\xe5\xad\xa6\xe4\xb9\xa0')], default=b'0', editable=False, max_length=12, verbose_name='\u5b66\u4e60\u72b6\u6001')),
                ('common_status', models.CharField(choices=[(b'0', b'\xe9\x9d\x9e\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98'), (b'1', b'\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98')], default=b'0', max_length=12, verbose_name='\u662f\u5426\u5e38\u89c1')),
                ('node', models.CharField(blank=True, default=b'', editable=False, max_length=100, verbose_name='\u8282\u70b9ID')),
                ('threshold', models.CharField(default=b'0.2', help_text='\u8bf7\u8f93\u51650~1\u7684\u503c\u3002', max_length=10, verbose_name='\u9608\u503c')),
            ],
            options={
                'verbose_name': '\u4e07\u8fbe',
                'verbose_name_plural': '\u4e07\u8fbe',
            },
        ),
        migrations.CreateModel(
            name='p16',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='\u95ee\u9898')),
                ('answer', models.CharField(max_length=500, verbose_name='\u7b54\u6848')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u52a0\u5165\u65f6\u95f4')),
                ('status', models.CharField(choices=[(b'0', b'\xe5\xbe\x85\xe5\xad\xa6\xe4\xb9\xa0'), (b'1', b'\xe5\xb7\xb2\xe5\xad\xa6\xe4\xb9\xa0')], default=b'0', editable=False, max_length=12, verbose_name='\u5b66\u4e60\u72b6\u6001')),
                ('common_status', models.CharField(choices=[(b'0', b'\xe9\x9d\x9e\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98'), (b'1', b'\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98')], default=b'0', max_length=12, verbose_name='\u662f\u5426\u5e38\u89c1')),
                ('node', models.CharField(blank=True, default=b'', editable=False, max_length=100, verbose_name='\u8282\u70b9ID')),
                ('threshold', models.CharField(default=b'0.2', help_text='\u8bf7\u8f93\u51650~1\u7684\u503c\u3002', max_length=10, verbose_name='\u9608\u503c')),
            ],
            options={
                'verbose_name': '\u4e0a\u56fe',
                'verbose_name_plural': '\u4e0a\u56fe',
            },
        ),
        migrations.CreateModel(
            name='p17',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='\u95ee\u9898')),
                ('answer', models.CharField(max_length=500, verbose_name='\u7b54\u6848')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u52a0\u5165\u65f6\u95f4')),
                ('status', models.CharField(choices=[(b'0', b'\xe5\xbe\x85\xe5\xad\xa6\xe4\xb9\xa0'), (b'1', b'\xe5\xb7\xb2\xe5\xad\xa6\xe4\xb9\xa0')], default=b'0', editable=False, max_length=12, verbose_name='\u5b66\u4e60\u72b6\u6001')),
                ('common_status', models.CharField(choices=[(b'0', b'\xe9\x9d\x9e\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98'), (b'1', b'\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98')], default=b'0', max_length=12, verbose_name='\u662f\u5426\u5e38\u89c1')),
                ('node', models.CharField(blank=True, default=b'', editable=False, max_length=100, verbose_name='\u8282\u70b9ID')),
                ('threshold', models.CharField(default=b'0.2', help_text='\u8bf7\u8f93\u51650~1\u7684\u503c\u3002', max_length=10, verbose_name='\u9608\u503c')),
            ],
            options={
                'verbose_name': '\u9a74\u5988\u5988',
                'verbose_name_plural': '\u9a74\u5988\u5988',
            },
        ),
        migrations.CreateModel(
            name='p18',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='\u95ee\u9898')),
                ('answer', models.CharField(max_length=500, verbose_name='\u7b54\u6848')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u52a0\u5165\u65f6\u95f4')),
                ('status', models.CharField(choices=[(b'0', b'\xe5\xbe\x85\xe5\xad\xa6\xe4\xb9\xa0'), (b'1', b'\xe5\xb7\xb2\xe5\xad\xa6\xe4\xb9\xa0')], default=b'0', editable=False, max_length=12, verbose_name='\u5b66\u4e60\u72b6\u6001')),
                ('common_status', models.CharField(choices=[(b'0', b'\xe9\x9d\x9e\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98'), (b'1', b'\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98')], default=b'0', max_length=12, verbose_name='\u662f\u5426\u5e38\u89c1')),
                ('node', models.CharField(blank=True, default=b'', editable=False, max_length=100, verbose_name='\u8282\u70b9ID')),
                ('threshold', models.CharField(default=b'0.2', help_text='\u8bf7\u8f93\u51650~1\u7684\u503c\u3002', max_length=10, verbose_name='\u9608\u503c')),
            ],
            options={
                'verbose_name': '\u4e30\u8da3\u6d77\u6dd8',
                'verbose_name_plural': '\u4e30\u8da3\u6d77\u6dd8',
            },
        ),
        migrations.CreateModel(
            name='p20',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='\u95ee\u9898')),
                ('answer', models.CharField(max_length=500, verbose_name='\u7b54\u6848')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u52a0\u5165\u65f6\u95f4')),
                ('status', models.CharField(choices=[(b'0', b'\xe5\xbe\x85\xe5\xad\xa6\xe4\xb9\xa0'), (b'1', b'\xe5\xb7\xb2\xe5\xad\xa6\xe4\xb9\xa0')], default=b'0', editable=False, max_length=12, verbose_name='\u5b66\u4e60\u72b6\u6001')),
                ('common_status', models.CharField(choices=[(b'0', b'\xe9\x9d\x9e\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98'), (b'1', b'\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98')], default=b'0', max_length=12, verbose_name='\u662f\u5426\u5e38\u89c1')),
                ('node', models.CharField(blank=True, default=b'', editable=False, max_length=100, verbose_name='\u8282\u70b9ID')),
                ('threshold', models.CharField(default=b'0.2', help_text='\u8bf7\u8f93\u51650~1\u7684\u503c\u3002', max_length=10, verbose_name='\u9608\u503c')),
            ],
            options={
                'verbose_name': '\u5185\u90e8\u6d4b\u8bd5\u7528\u4f8b',
                'verbose_name_plural': '\u5185\u90e8\u6d4b\u8bd5\u7528\u4f8b',
            },
        ),
        migrations.CreateModel(
            name='p24',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='\u95ee\u9898')),
                ('answer', models.CharField(max_length=500, verbose_name='\u7b54\u6848')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u52a0\u5165\u65f6\u95f4')),
                ('status', models.CharField(choices=[(b'0', b'\xe5\xbe\x85\xe5\xad\xa6\xe4\xb9\xa0'), (b'1', b'\xe5\xb7\xb2\xe5\xad\xa6\xe4\xb9\xa0')], default=b'0', editable=False, max_length=12, verbose_name='\u5b66\u4e60\u72b6\u6001')),
                ('common_status', models.CharField(choices=[(b'0', b'\xe9\x9d\x9e\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98'), (b'1', b'\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98')], default=b'0', max_length=12, verbose_name='\u662f\u5426\u5e38\u89c1')),
                ('node', models.CharField(blank=True, default=b'', editable=False, max_length=100, verbose_name='\u8282\u70b9ID')),
                ('threshold', models.CharField(default=b'0.2', help_text='\u8bf7\u8f93\u51650~1\u7684\u503c\u3002', max_length=10, verbose_name='\u9608\u503c')),
            ],
            options={
                'verbose_name': 'yoyo',
                'verbose_name_plural': 'yoyo',
            },
        ),
        migrations.CreateModel(
            name='p26',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='\u95ee\u9898')),
                ('answer', models.CharField(max_length=500, verbose_name='\u7b54\u6848')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u52a0\u5165\u65f6\u95f4')),
                ('status', models.CharField(choices=[(b'0', b'\xe5\xbe\x85\xe5\xad\xa6\xe4\xb9\xa0'), (b'1', b'\xe5\xb7\xb2\xe5\xad\xa6\xe4\xb9\xa0')], default=b'0', editable=False, max_length=12, verbose_name='\u5b66\u4e60\u72b6\u6001')),
                ('common_status', models.CharField(choices=[(b'0', b'\xe9\x9d\x9e\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98'), (b'1', b'\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98')], default=b'0', max_length=12, verbose_name='\u662f\u5426\u5e38\u89c1')),
                ('node', models.CharField(blank=True, default=b'', editable=False, max_length=100, verbose_name='\u8282\u70b9ID')),
                ('threshold', models.CharField(default=b'0.2', help_text='\u8bf7\u8f93\u51650~1\u7684\u503c\u3002', max_length=10, verbose_name='\u9608\u503c')),
            ],
            options={
                'verbose_name': '\u9752\u521b\u5de5\u573a',
                'verbose_name_plural': '\u9752\u521b\u5de5\u573a',
            },
        ),
        migrations.CreateModel(
            name='p27',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='\u95ee\u9898')),
                ('answer', models.CharField(max_length=500, verbose_name='\u7b54\u6848')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u52a0\u5165\u65f6\u95f4')),
                ('status', models.CharField(choices=[(b'0', b'\xe5\xbe\x85\xe5\xad\xa6\xe4\xb9\xa0'), (b'1', b'\xe5\xb7\xb2\xe5\xad\xa6\xe4\xb9\xa0')], default=b'0', editable=False, max_length=12, verbose_name='\u5b66\u4e60\u72b6\u6001')),
                ('common_status', models.CharField(choices=[(b'0', b'\xe9\x9d\x9e\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98'), (b'1', b'\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98')], default=b'0', max_length=12, verbose_name='\u662f\u5426\u5e38\u89c1')),
                ('node', models.CharField(blank=True, default=b'', editable=False, max_length=100, verbose_name='\u8282\u70b9ID')),
                ('threshold', models.CharField(default=b'0.2', help_text='\u8bf7\u8f93\u51650~1\u7684\u503c\u3002', max_length=10, verbose_name='\u9608\u503c')),
            ],
            options={
                'verbose_name': '\u4e1c\u65b9\u91d1\u878d',
                'verbose_name_plural': '\u4e1c\u65b9\u91d1\u878d',
            },
        ),
        migrations.CreateModel(
            name='p28',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='\u95ee\u9898')),
                ('answer', models.CharField(max_length=500, verbose_name='\u7b54\u6848')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u52a0\u5165\u65f6\u95f4')),
                ('status', models.CharField(choices=[(b'0', b'\xe5\xbe\x85\xe5\xad\xa6\xe4\xb9\xa0'), (b'1', b'\xe5\xb7\xb2\xe5\xad\xa6\xe4\xb9\xa0')], default=b'0', editable=False, max_length=12, verbose_name='\u5b66\u4e60\u72b6\u6001')),
                ('common_status', models.CharField(choices=[(b'0', b'\xe9\x9d\x9e\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98'), (b'1', b'\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98')], default=b'0', max_length=12, verbose_name='\u662f\u5426\u5e38\u89c1')),
                ('node', models.CharField(blank=True, default=b'', editable=False, max_length=100, verbose_name='\u8282\u70b9ID')),
                ('threshold', models.CharField(default=b'0.2', help_text='\u8bf7\u8f93\u51650~1\u7684\u503c\u3002', max_length=10, verbose_name='\u9608\u503c')),
            ],
            options={
                'verbose_name': '\u8bfa\u5143\u91d1\u878d',
                'verbose_name_plural': '\u8bfa\u5143\u91d1\u878d',
            },
        ),
        migrations.CreateModel(
            name='p30',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='\u95ee\u9898')),
                ('answer', models.CharField(max_length=500, verbose_name='\u7b54\u6848')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u52a0\u5165\u65f6\u95f4')),
                ('status', models.CharField(choices=[(b'0', b'\xe5\xbe\x85\xe5\xad\xa6\xe4\xb9\xa0'), (b'1', b'\xe5\xb7\xb2\xe5\xad\xa6\xe4\xb9\xa0')], default=b'0', editable=False, max_length=12, verbose_name='\u5b66\u4e60\u72b6\u6001')),
                ('common_status', models.CharField(choices=[(b'0', b'\xe9\x9d\x9e\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98'), (b'1', b'\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98')], default=b'0', max_length=12, verbose_name='\u662f\u5426\u5e38\u89c1')),
                ('node', models.CharField(blank=True, default=b'', editable=False, max_length=100, verbose_name='\u8282\u70b9ID')),
                ('threshold', models.CharField(default=b'0.2', help_text='\u8bf7\u8f93\u51650~1\u7684\u503c\u3002', max_length=10, verbose_name='\u9608\u503c')),
            ],
            options={
                'verbose_name': 'E-AI',
                'verbose_name_plural': 'E-AI',
            },
        ),
        migrations.CreateModel(
            name='p31',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='\u95ee\u9898')),
                ('answer', models.CharField(max_length=500, verbose_name='\u7b54\u6848')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u52a0\u5165\u65f6\u95f4')),
                ('status', models.CharField(choices=[(b'0', b'\xe5\xbe\x85\xe5\xad\xa6\xe4\xb9\xa0'), (b'1', b'\xe5\xb7\xb2\xe5\xad\xa6\xe4\xb9\xa0')], default=b'0', editable=False, max_length=12, verbose_name='\u5b66\u4e60\u72b6\u6001')),
                ('common_status', models.CharField(choices=[(b'0', b'\xe9\x9d\x9e\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98'), (b'1', b'\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98')], default=b'0', max_length=12, verbose_name='\u662f\u5426\u5e38\u89c1')),
                ('node', models.CharField(blank=True, default=b'', editable=False, max_length=100, verbose_name='\u8282\u70b9ID')),
                ('threshold', models.CharField(default=b'0.2', help_text='\u8bf7\u8f93\u51650~1\u7684\u503c\u3002', max_length=10, verbose_name='\u9608\u503c')),
            ],
            options={
                'verbose_name': '\u4e0a\u4ea4\u4f1a',
                'verbose_name_plural': '\u4e0a\u4ea4\u4f1a',
            },
        ),
        migrations.CreateModel(
            name='p32',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='\u95ee\u9898')),
                ('answer', models.CharField(max_length=500, verbose_name='\u7b54\u6848')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u52a0\u5165\u65f6\u95f4')),
                ('status', models.CharField(choices=[(b'0', b'\xe5\xbe\x85\xe5\xad\xa6\xe4\xb9\xa0'), (b'1', b'\xe5\xb7\xb2\xe5\xad\xa6\xe4\xb9\xa0')], default=b'0', editable=False, max_length=12, verbose_name='\u5b66\u4e60\u72b6\u6001')),
                ('common_status', models.CharField(choices=[(b'0', b'\xe9\x9d\x9e\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98'), (b'1', b'\xe5\xb8\xb8\xe8\xa7\x81\xe9\x97\xae\xe9\xa2\x98')], default=b'0', max_length=12, verbose_name='\u662f\u5426\u5e38\u89c1')),
                ('node', models.CharField(blank=True, default=b'', editable=False, max_length=100, verbose_name='\u8282\u70b9ID')),
                ('threshold', models.CharField(default=b'0.2', help_text='\u8bf7\u8f93\u51650~1\u7684\u503c\u3002', max_length=10, verbose_name='\u9608\u503c')),
            ],
            options={
                'verbose_name': '\u6d4b\u8bd5123',
                'verbose_name_plural': '\u6d4b\u8bd5123',
            },
        ),
    ]
