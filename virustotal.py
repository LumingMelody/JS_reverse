# -*- coding: utf-8 -*-
# @Time    : 2023/3/14 17:32
# @Author  : 蔍鸣霸霸
# @FileName: virustotal.py
# @Software: PyCharm
# @Blog    ：只因你太美

import execjs
import requests
from lxpy import copy_headers_dict

url = 'https://www.virustotal.com/ui/search?limit=20&relationships%5Bcomment%5D=author%2Citem&query=1'
headers = copy_headers_dict('''
accept: application/json
accept-encoding: gzip, deflate, br
accept-ianguage: en-US,en;q=0.9,es;q=0.8
accept-language: zh-CN,zh;q=0.9
content-type: application/json
cookie: _ga=GA1.2.747208657.1642417044; _gid=GA1.2.988701706.1642417044
referer: https://www.virustotal.com/
sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36
x-app-version: v1x57x0
x-tool: vt-ui-main
''')

js = '''
function get_anti(){
            const e = Date.now() / 1e3;
             return Buffer.from((`${(()=>{
                const e = 1e10 * (1 + Math.random() % 5e4);
                return e < 50 ? "-1" : e.toFixed(0)
            }
            )()}-ZG9udCBiZSBldmls-${e}`)).toString('base64');
        }
'''
xvt_anti = execjs.compile(js).call('get_anti')
headers.update({'x-vt-anti-abuse-header':xvt_anti})

print(requests.get(url, headers=headers).text)