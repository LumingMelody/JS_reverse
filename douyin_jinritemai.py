# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 14:24
# @Author  : 蔍鸣霸霸
# @FileName: douyin_jinritemai.py
# @Software: PyCharm
# @Blog    ：只因你太美

import requests
import execjs


def get_sign(url):
    with open('./js_signature/jinritemai.js', 'r', encoding='utf-8') as f:
        js = f.read()
    sign = execjs.compile(js).call('get_sign', url)
    return sign


url = '/api/svc/list?cate_id=47&order_by=sale_num&page_index=0&page_size=30'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
}
new_url = get_sign(url)
print(new_url)
print(requests.get(new_url, headers=headers).text)

