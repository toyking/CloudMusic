# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render

from NetEaseCloudMusic.api import NetEaseCloudMusicApi


def index(request):
    return render(request, 'index.html')


def home(request):
    ret_song_personalized = NetEaseCloudMusicApi.send_request('personalized', method='GET', data={'limit': 6})
    ret_new_song_personalized = NetEaseCloudMusicApi.send_request('personalized/newsong', method='GET', data={})
    context = {
        'song_personalized': ret_song_personalized.get('result'),
        'new_song_personalized': ret_new_song_personalized.get('result'),
    }
    return render(request, 'home.html', context)


def login(request):
    return render(request, 'login.html')


def hot_music_list(request):
    return render(request, 'login.html')


def top_mv(request):
    limit = request.GET.get('limit', 20)
    if not limit:
        return JsonResponse({'code': -1, 'msg': 'params error', 'data': []})

    ret = NetEaseCloudMusicApi.send_request('top/mv', method='GET', data={'limit': limit})
    context = {'top_mv_list': ret['data']}
    return render(request, 'top_mv.html', context)


def song_detail(request):
    song_id = request.GET.get('id')
    if not song_id:
        return JsonResponse({'code': -1, 'msg': 'params error', 'data': []})

    ret_song_detail = NetEaseCloudMusicApi.send_request('song/detail', method='GET', data={'ids': song_id})
    ret_song_url = NetEaseCloudMusicApi.send_request('song/url', method='GET', data={'id': song_id})
    ret_song_comment = NetEaseCloudMusicApi.send_request('comment/music', method='GET', data={'id': song_id})

    context = {
        'song_detail': ret_song_detail.get('songs')[0],
        'song_url': ret_song_url.get('data')[0],
        'song_comment': ret_song_comment.get('hotComments'),
    }

    return render(request, 'song_detail.html', context)


def mv_detail(request):
    mv_id = request.GET.get('id')
    if not mv_id:
        return JsonResponse({'code': -1, 'msg': 'params error', 'data': []})

    ret_mv_detail = NetEaseCloudMusicApi.send_request('mv/detail', method='GET', data={'mvid': mv_id})
    ret_mv_comment = NetEaseCloudMusicApi.send_request('comment/mv', method='GET', data={'id': mv_id})

    context = {
        'mv_detail': ret_mv_detail['data'],
        'mv_comment': ret_mv_comment['hotComments'],
    }

    return render(request, 'mv_detail.html', context)


def login_post(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    ctx = {}
    if not username or not password:
        ctx['error_msg'] = u'错误的用户名密码'
        return render(request, 'login.html', ctx)

    return render(request, 'index.html', ctx)
