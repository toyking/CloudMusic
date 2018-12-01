# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def hot_music_list(request):
    return render(request, 'login.html')


def login_post(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    ctx = {}
    if not username or not password:
        ctx['error_msg'] = u'错误的用户名密码'
        return render(request, 'login.html', ctx)

    return render(request, 'index.html', ctx)
