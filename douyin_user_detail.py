#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re
from urllib import parse
import requests
import execjs


def get_ac_sign(ac_nonce):
    with open('./js_signature/_ac_signature.js', 'r', encoding='utf-8') as f:
        b = f.read()
    c = execjs.compile(b)
    d = c.call('get_ac_signature', ac_nonce)
    return d


def run(sec_user_id):
    sess = requests.session()
    headers_base = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    __ac_nonce = sess.get('https://www.douyin.com/', headers=headers_base).cookies.get('__ac_nonce')
    print(__ac_nonce)

    url = f"https://www.douyin.com/user/{sec_user_id}"
    __ac_signature = get_ac_sign(__ac_nonce)
    headers = {
        'authority': 'www.douyin.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9,en-XA;q=0.8,en;q=0.7,zh-TW;q=0.6',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'cookie': f'douyin.com; __ac_nonce={__ac_nonce}; __ac_signature={__ac_signature};',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    ttwid = sess.get('https://www.douyin.com/', headers=headers).cookies.get('ttwid')
    print(ttwid)

    headers.update({
                       'cookie': f'__ac_referer=https://www.douyin.com/user/{sec_user_id}; douyin.com; __ac_nonce={__ac_nonce}; __ac_signature={__ac_signature}; passport_csrf_token=7bced54d39291bf977d263d082a365c9; passport_csrf_token_default=7bced54d39291bf977d263d082a365c9; ttwid={ttwid};'})
    response = sess.get(url, headers=headers)
    doc = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script>', response.text, re.S)[0]
    data = json.loads(parse.unquote(doc))
    return data


if __name__ == '__main__':
    sec_user_id = "MS4wLjABAAAAYmudsq_brPKh7R5rDQwj4pVP11x_gMLM2zqnZj1wc8Q"
    data = run(sec_user_id)
    if data.get('41'):
        print(data['41']['user'])       # IP地址、年龄、粉丝信息等
        print(data['41']['post'])       # 作品列表、bitRateList
