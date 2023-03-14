# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 15:26
# @Author  : 蔍鸣霸霸
# @FileName: fse.py
# @Software: PyCharm
# @Blog    ：只因你太美

import requests
import execjs

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "fse-api.agilestudio.cn",
    "Origin": "https://fse.agilestudio.cn",
    "Pragma": "no-cache",
    "Referer": "https://fse.agilestudio.cn/",
    "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
}

with open('./js_signature/fse33.js', 'r', encoding='utf-8') as f:
    js = f.read()
params, sign = execjs.compile(js).call('get_sign', '火车')

headers.update({'X-Signature': sign})

url = 'https://fse-api.agilestudio.cn/api/search?' + params.replace(',', '&')

print(requests.get(url, headers=headers).text)
