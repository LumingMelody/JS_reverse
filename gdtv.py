# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 17:35
# @Author  : 蔍鸣霸霸
# @FileName: gdtv.py
# @Software: PyCharm
# @Blog    ：只因你太美

# -*- coding: UTF-8 -*-

import hmac
import base64, random
from hashlib import sha256
import time

import requests


def get_headers(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'origin': 'https://www.gdtv.cn',
        'referer': 'https://www.gdtv.cn/',
        'x-itouchtv-ca-key': '89541443007807288657755311869534',
        'x-itouchtv-client': 'WEB_PC',
    }
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    device_id = 'WEB_1068fae0-504e-11ed-82cf-' + ''.join([random.choice(base_str) for i in range(12)])
    headers.update({'x-itouchtv-device-id': device_id})
    d = str(int(time.time() * 1000))
    v = 'GET\n' + url + '\n' + d + '\n'
    k = 'dfkcY1c3sfuw0Cii9DWjOUO3iQy2hqlDxyvDXd1oVMxwYAJSgeB6phO8eW1dfuwX'.encode('utf-8')
    signature = str(base64.b64encode(hmac.new(k, v.encode('utf-8'), digestmod=sha256).digest()), 'utf-8')
    headers.update({'x-itouchtv-ca-signature': signature, 'x-itouchtv-ca-timestamp': d})
    return headers


def get_data(url):
    headers = get_headers(url)
    response = requests.get(url, headers=headers).json()
    print(response)


if __name__ == '__main__':
    url = 'https://gdtv-api.gdtv.cn/api/channel/v1/news?beginScore=0&pageSize=7&channelId=109'
    get_data(url)
