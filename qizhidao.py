# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 16:35
# @Author  : 蔍鸣霸霸
# @FileName: qizhidao.py
# @Software: PyCharm
# @Blog    ：只因你太美

import base64
# from Crypto.Cipher import AES
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad
import requests, execjs


def decrypt(data):
    html = base64.b64decode(data)
    key = b'xc46VoB49X3PGYAg'
    aes = AES.new(key=key, mode=AES.MODE_ECB)
    info = aes.decrypt(html)
    decrypt_data = unpad(info, 16).decode()
    return decrypt_data


def webid():
    js = '''
    const crypto = require('crypto');

window = {}
window.navigator ={
    userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

function md5(data){
    return crypto.createHash('md5').update(String(data)).digest('hex');
}

function z_i() {
    var t = undefined;
    var e = (t || window.navigator.userAgent || Object(a_m)(4, 8)) + (new Date).getTime() + Object(a_m)(4, 8);
    return 'X/'.concat(md5(e))
}

function a_m(t, e, n) {
    var r, o = "";
    void 0 === t && (t = 6),
    "string" == typeof e && (n = e),
    r = e && "number" == typeof e ? Math.round(Math.random() * (e - t)) + t : t,
    n = n || "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    for (var i = 0; i < r; i++) {
        var a = Math.round(Math.random() * (n.length - 1));
        o += n.substring(a, a + 1)
    }
    return o
}
    '''
    exec = execjs.compile(js)
    return exec.call('z_i')


h = {
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://www.qizhidao.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "user-agent-web": webid(),
}
data = {"content": "中科大数据研究院", "app_date_list": [], "cur_legal_status_list": [], "out_types": [],
        "pageSize": 20, "current": 1, "orderColumn": "_score", "orderType": "DESC", "platform": 1}
r = requests.post('https://www.qizhidao.com/api/qzd-bff-ips/patent/search/list', headers=h, json=data)
print(decrypt(r.json()['data1']))
