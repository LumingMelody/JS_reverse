# -*- coding: utf-8 -*-
# @Time    : 2023/4/5 13:47
# @Author  : 蔍鸣霸霸
# @FileName: sdx.py
# @Software: PyCharm
# @Blog    ：只因你太美


import json
import random
import hashlib
import time
import requests


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


def get_sign():
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
    md5_str = md5_hash.hexdigest()

    # print("MD5 哈希值：", md5_str)
    return ms_timestamp, t, md5_str


def get_list(page_num):
    ms_timestamp, t, md5_str = get_sign()
    url = f'https://int.51sdx.com/niuzy/uinfo/univ/queryUniv?univName=&provId=&univType=&zbType=&departType=&isPublic=&feature=&is985=&is211=&isFirstClass=&isFirstLevel=&hasMaster=&isIndependent=&pageSize=10&pageNum={page_num}&verifyTimestamp={ms_timestamp}&verifyNonce={t}&channel=sdx&channelId=sdx&channelCode=sdx&comeFrom=&verifySign={md5_str}'
    response = requests.get(url, headers=headers, cookies=cookies)
    print(response.json())


if __name__ == '__main__':
    for page in range(1, 3):
        get_list(page)
