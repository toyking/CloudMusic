# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render

from NetEaseCloudMusic.api import NetEaseCloudMusicApi


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def hot_music_list(request):
    return render(request, 'login.html')


def top_mv(request):
    limit = request.GET.get('limit', 10)
    if not limit:
        return JsonResponse({'code': -1, 'msg': 'params error', 'data': []})

    ret = NetEaseCloudMusicApi.send_request('top/mv', method='GET', data={'limit': 10})
    context = {'top_mv_list': ret['data']}
    return render(request, 'top_mv.html', context)


def login_post(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    ctx = {}
    if not username or not password:
        ctx['error_msg'] = u'错误的用户名密码'
        return render(request, 'login.html', ctx)

    return render(request, 'index.html', ctx)
