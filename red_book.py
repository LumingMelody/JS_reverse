# -*- coding: utf-8 -*-
# @Time    : 2023/3/8 14:51
# @Author  : 蔍鸣霸霸
# @FileName: red_book.py
# @Software: PyCharm
# @Blog    ：只因你太美

import requests
import execjs
import random


def register_webId():
    s = "abcdef0123456789"
    webId = ''
    for i in range(32):
        webId += random.choice(s)
    return webId


def register_session():
    url = 'https://edith.xiaohongshu.com/api/sns/web/v1/login/activate'
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
        "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "cookie": f"webId={register_webId()};",
        "origin": "https://www.xiaohongshu.com",
        "pragma": "no-cache",
        "referer": "https://www.xiaohongshu.com/",
        "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "x-s": "ZYw6sYaJOi1COiaB1BTpsjvCZg1ls2F+ZgA+sBMWZgM3",
        "x-t": "1675323769927"
    }
    session = requests.post(url, data='{}', headers=headers).json()['data']['session']
    return session


def feed(source_note_id):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
        "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "cookie": f"web_session=030037a33b64c05ce976f87670234ae4c46c64",
        # "cookie":f"web_session={register_session()}",  # web_session和当前IP或者环境绑定，重新注册后浏览器中的ID也会更新
        "origin": "https://www.xiaohongshu.com",
        "pragma": "no-cache",
        "referer": "https://www.xiaohongshu.com/",
        "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "x-s": "1lqJsBVUOjsiO6dk1BspOg9G16O6sgAWslOJ1gkvOgF3",
        "x-t": "1675387207946"
    }
    with open('js_signature/xhs_xt.js', 'r', encoding='utf-8') as f:
        js = f.read()
    crt = execjs.compile(js)
    data = '{"source_note_id":"%s"}' % source_note_id
    xs_xt = crt.call('sign', '/api/sns/web/v1/feed', {"source_note_id": "%s" % source_note_id})
    xs_xt['X-t'] = str(xs_xt['X-t'])

    headers.update(xs_xt)
    feed = 'https://edith.xiaohongshu.com/api/sns/web/v1/feed'
    print(requests.post(url=feed, data=data, headers=headers).text)


print(register_session())

# feed("63cf8afe000000001f023d49")
