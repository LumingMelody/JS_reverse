# -*- coding: utf-8 -*-
# @Time    : 2023/4/21 11:21
# @Author  : 蔍鸣霸霸
# @FileName: boss_test.py
# @Software: PyCharm
# @Blog    ：只因你太美
import execjs

with open('./js_signature/boss补环境.js', 'r', encoding='utf-8') as f:
    js = f.read()
sign = execjs.compile(js).call('getSign')
print(sign)