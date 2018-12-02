# -*- coding: utf-8 -*-
import datetime
import json
import requests

from NetEaseCloudMusic.config import NET_EASE_CLOUD_MUSIC_API_SERVER_URL


class NetEaseCloudMusicApi:

    def __init__(self):
        pass

    @staticmethod
    def send_request(url, method='GET', data=None):
        time_start = datetime.datetime.now()
        _url = NET_EASE_CLOUD_MUSIC_API_SERVER_URL + url
        try:
            if method == 'GET':
                response = requests.get(_url, params=data, timeout=30)
            else:
                response = requests.post(_url, data=json.dumps(data), timeout=30)
            print "REQUEST URL: %s\nMETHOD: %s\nREQUEST: %s" % (response.url, method, data)
            if not response or response.status_code != 200:
                print "HTTP_CODE: %s" % response.status_code
                return {}
            result = response.json()
        except Exception as err:
            print "REQUEST http exception, err:%s" % err
            return {}

        time_cost = (datetime.datetime.now() - time_start).total_seconds()
        print "RESPONSE: %s\nTIME_COST: %s seconds" % (result, time_cost)

        return result
