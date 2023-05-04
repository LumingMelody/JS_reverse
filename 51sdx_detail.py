# -*- coding: utf-8 -*-
# @Time    : 2023/4/5 15:35
# @Author  : 蔍鸣霸霸
# @FileName: 51sdx_detail.py
# @Software: PyCharm
# @Blog    ：只因你太美

import hashlib
import json
import random
import time
import execjs
import requests
from sdx import get_sign
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.append([
    '年份', '招生类型', '招生批次', '院校(招生方向)', '科目要求', '录取人数', '最低分/位次', '平均分/位次', '最高分/位次'
])

headers = {
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://www.51sdx.com/',
    'Sec-Fetch-Dest': 'image',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.51sdx.com',
    'authority': 'static.51sdx.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'Hm_lvt_e3883fb2fc50eb402dd97dc699db074c=1680598679; Hm_lpvt_e3883fb2fc50eb402dd97dc699db074c=1680621998',
    'pragma': 'no-cache',
    'referer': 'https://www.51sdx.com/',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}


def get_verifysign():
    ms_timestamp = str(time.time() * 1000)
    userdata_cookie = "{}"  # replace with actual cookie string
    userdata = json.loads(userdata_cookie)
    hexUnid = userdata.get("hexUnid", "")
    random_number = str(random.randint(0, 999999)).zfill(6)
    t = hexUnid + random_number
    # print(t)

    # 使用 hashlib 计算 MD5 哈希值
    m_str = ms_timestamp + "_" + t + "_sdxxqbrolkjwrgoiuyhasdglksjlaghnow32429asnnhg"
    # m_str = "1680673332300_242969_sdxxqbrolkjwrgoiuyhasdglksjlaghnow32429asnnhg"
    md5_hash = hashlib.md5(m_str.encode())

    # 将结果转换为十六进制字符串
    verify_sign = md5_hash.hexdigest()

    # print("MD5 哈希值：", md5_str)
    return ms_timestamp, t, verify_sign


def get_param_sign(univ_id):
    # m_str = t_univId + t_provinceId + '25raHVwZ2xnemhsbW9jdHBkbGRkZ2dka2pkdG92aHB3ZGVoYHBoAAA'
    m_str = f'{univ_id}125raHVwZ2xnemhsbW9jdHBkbGRkZ2dka2pkdG92aHB3ZGVoYHBoAAA'
    # '10141125raHVwZ2xnemhsbW9jdHBkbGRkZ2dka2pkdG92aHB3ZGVoYHBoAAA'
    md5_hash = hashlib.md5(m_str.encode())

    # 将结果转换为十六进制字符串
    param_sign = md5_hash.hexdigest()
    # print(param_sign)
    return param_sign


def get_detail(page_num):
    ms_timestamp, t, verify_sign = get_verifysign()
    url = f'https://int.51sdx.com/niuzy/uinfo/univ/queryUniv?univName=&provId=&univType=&zbType=&departType=&isPublic=&feature=&is985=&is211=&isFirstClass=&isFirstLevel=&hasMaster=&isIndependent=&pageSize=10&pageNum={page_num}&verifyTimestamp={ms_timestamp}&verifyNonce={t}&channel=sdx&channelId=sdx&channelCode=sdx&comeFrom=&verifySign={verify_sign}'
    list_response = requests.get(url, headers=headers).json()
    items = list_response['data']
    for item in items:
        univ_id = item['univId']
        ms_timestamp, t, verifysign = get_sign()
        param_sign = get_param_sign(univ_id)
        url = f'https://int.51sdx.com/niuzy/uinfo/univ/univEnrollList?customerId=&provinceId=1&univId={univ_id}&tenantId=0&paramSign={param_sign}&verifyTimestamp={ms_timestamp}&verifyNonce={t}&channel=sdx&channelId=sdx&channelCode=sdx&comeFrom=&verifySign={verifysign}&majorTypeId=2'
        response = requests.get(url, headers=headers)
        # print(response.json())
        with open(r'./js_signature/51sdx_parse.js', 'r', encoding='utf-8') as f:
            js_str = f.read()
        data = execjs.compile(js_str).call('parseData', response.json()['data'])
        for d in data:
            print(d)
            # 年份
            year = d.get('year', '-')
            # 招生类型
            enrolled = '普通类'
            # 招生批次
            batch_name = d.get('batchName', '-')
            # 院校(招生方向)
            univ_name = d.get('univName', '-')
            # 科目要求
            subject = '理科'
            # 录取人数
            enroll_num = d.get('enrolled', '-')
            # 最低分 / 位次
            low_score = d.get('lowScore', '-')
            low_rank = d.get('lowRank', '-')
            low_score_rank = str(low_score) + '/' + str(low_rank)
            # 平均分 / 位次
            avg_score = d.get('averageScore', '-')
            avg_rank = d.get('averageRank', '-')
            avg_score_rank = str(avg_score) + '/' + str(avg_rank)
            # 最高分 / 位次
            high_score = d.get('highScore', '-')
            high_rank = d.get('highRank', '-')

            high_score_rank = str(high_score) + '/' + str(high_rank)
            ws.append([year, enrolled, batch_name, univ_name, subject, enroll_num, low_score_rank, avg_score_rank,
                       high_score_rank])
        wb.save(r'./data/51sdx_detail.xlsx')


if __name__ == '__main__':
    for page in range(1, 31):
        print("当前页数：", page)
        get_detail(page)
        time.sleep(2)
