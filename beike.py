# -*- coding: utf-8 -*-
# @Time    : 2023/3/10 18:28
# @Author  : 蔍鸣霸霸
# @FileName: beike.py
# @Software: PyCharm
# @Blog    ：只因你太美
import json
import execjs
import requests

cookies = {
    'select_city': '110000',
    'lianjia_uuid': '55894941-66a6-4204-8e5c-032cb2b5194a',
    'sajssdk_2015_cross_new_user': '1',
    'lianjia_ssid': '3a62efc0-c1b3-4455-9b3b-1a377e05b6cb',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22186ca6216a06f7-032abd06edd4d4-1f525634-2073600-186ca6216a11ab0%22%2C%22%24device_id%22%3A%22186ca6216a06f7-032abd06edd4d4-1f525634-2073600-186ca6216a11ab0%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://bj.ke.com',
    'Pragma': 'no-cache',
    'Referer': 'https://bj.ke.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}
data = '{"service":"https://ajax.api.ke.com/login/login/getuserinfo","version":"2.0"}'

response = requests.post('https://clogin.ke.com/authentication/initialize', headers=headers, cookies=cookies, data=data)

with open(r'./js_signature/beike.js', 'r', encoding='utf-8') as f:
    js_str = f.read()
password = execjs.compile(js_str).call('get_password', 'xu123456')
# print(password)

data = {
    "service": "https://ajax.api.ke.com/login/login/getuserinfo", "mainAuthMethodName": "username-password",
    "accountSystem": "customer", "credential": {"username": "15358491819", "password": "': '", "encodeVersion": "1"},
    "context": {
        "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "clientSource": "pc", "os": "Mac OS", "osVersion": "10.15.7", "registerPosLx": 690, "registerPosLy": 227,
        "registerPosRx": 990, "registerPosRy": 277, "clickPosX": 804, "clickPosY": 252, "screen": "1680_331"},
    "loginTicketId": response.json().get('loginTicketId'), "version": "2.0",
    "srcId": "eyJ0Ijoie1wiZGF0YVwiOlwiMzAzNTY3OTYzMDRhZTlkNDc2ODI0YTUxNDUyMGU1MjI3NjZiODM4NDZjMjRiZjRiMDMwYWU1YmMzNjg2M2I3YzNmOWM3MzJjMGRkODM0ZWNjNjliNmY4YmE3ZjNmODk4NTY4NjcyMmExMjQzZDNlMmFkNTc1MzY3NjUxMjk3NTVkMzU5ZWI5MTdmMWUyZjdjMmQ1YjIzNTBlNGY2OThiNTA4OGQ3NjM1OTljYmViNTg4OTIwNDZhMDAxYjFiOTRhN2M4MWQ3MWQ5YjAxOGU4MDYzYTI1NWEwNTkzYzIzZmU3ZTdmZTE1Y2IyMGU4NTc1YzcxNDQ2MjlkYTZjNDFkM1wiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJhYjFmZmNmOFwifSIsInIiOiJodHRwczovL2JqLmtlLmNvbS8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==",
    "ticketMaxAge": 604800
}

data['credential']['password'] = password
data = json.dumps(data)
resp = requests.post('https://clogin.ke.com/authentication/authenticate', headers=headers, cookies=cookies, data=data)
print(resp.text)
