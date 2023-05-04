# -*- coding: utf-8 -*-
# @Time    : 2023/3/15 17:56
# @Author  : 蔍鸣霸霸
# @FileName: cnvd.py
# @Software: PyCharm
# @Blog    ：只因你太美
import json

import requests
import re
import execjs

# headers = {
#     # 如果被拦截，把headers补齐
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
#
# }
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.cnvd.org.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://www.cnvd.org.cn/flaw/list?flag=true',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}


sess = requests.session()
url = 'https://www.cnvd.org.cn/flaw/list.htm'


def start():
    r = sess.get(url, headers=headers, verify=False)
    text = r.text
    cookie = re.search('<script>document.cookie=(.*?);location', text).group(1)
    x = execjs.eval(cookie).split(';')[0].split('=')
    sess.cookies[x[0]] = x[1]
    print(x[0], x[1])


def then():
    '''获取第二次请求的cookie'''
    r1 = sess.get(url, headers=headers, verify=False)
    text = r1.text
    data = re.search(';go\((.*?)\)</script>', text).group(1)
    hash = re.search('"ha":"(.*?)",', data).group(1)
    # get_cookie_2是执行JS，完整代码请下载
    cookie = get_cookie_2(data, hash).split(';')[0].split('=')
    sess.cookies[cookie[0]] = cookie[1]


def end(page=1):
    data = {'number': '请输入精确编号', 'startDate': '', 'endDate': '', 'field': '', 'order': '', 'numPerPage': '10',
            'offset': page * 10, 'max': '10'}
    data = json.dumps(data)
    r1 = sess.post('https://www.cnvd.org.cn/flaw/list.htm?flag=true', headers=headers, data=data, verify=False)
    print(r1.text)


def get_cookie_2(data, hash):
    node = execjs.get()
    path = f'./js_signature/t_{hash}.js'
    with open(path, 'r', encoding='utf-8') as f:
        ctx = node.compile(f.read())
        funcName = f'go({data})'
        pwd = ctx.eval(funcName)
        return pwd


if __name__ == '__main__':
    start()
    then()
    end()
