# -*- coding: utf-8 -*-
# @Time    : 2023/6/20 11:39
# @Author  : 蔍鸣霸霸
# @FileName: meituan_live_goods.py
# @Software: PyCharm
# @Blog    ：只因你太美

import requests

cookies = {
    'WEBDFPID': '3711zz4320u05x610y09v9u96421433y811w7yy4y99979589zuuwzxy-2002522673938-1687162673557GGUKGQQ75613c134b6a252faa6802015be905512802',
    '_lxsdk_cuid': '188d2bb5b52c8-0a03e17be32c39-1b525634-1fa400-188d2bb5b53c8',
    '_lxsdk': '188d2bb5b52c8-0a03e17be32c39-1b525634-1fa400-188d2bb5b53c8',
    '_lx_utm': 'utm_source%3Dshare%26utm_term%3DAiphoneBgroupC12.10.402DcopyEpromotionG0000000000000A4E8031D358C41A89BCF3B1774A246ACA16328709257531513920230619162043348%26utm_medium%3DiOSweb',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}


def get_data(url):
    response = requests.get(url, headers=headers).json()
    print(response)
    goods_list = response['data']['goodsList']
    for goods in goods_list:
        title = goods['title']
        market_price = goods['marketPrice']
        price = goods['price']
        pic = goods['picUrl']


if __name__ == '__main__':
    m_url = 'https://mlive.meituan.com/api/mlive/promotion/goods/mlivelistgoods.bin?platform=2&appid=10&inapp=false&liveid=277130&cityid=80&lat=31.273493&lng=120.587219&requestType=0&extraInfo=%257B%2522pageSource%2522%253A%2522zhibo_share%2522%252C%2522squareSource%2522%253A%2522%2522%257D&selectedLat=31.273493&selectedLng=120.587219&poiId=&publicDomain=&yodaReady=h5&csecplatform=4&csecversion=2.0.0'
    get_data(m_url)
