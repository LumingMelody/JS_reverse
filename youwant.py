# -*- coding: utf-8 -*-
# @Time    : 2023/3/8 15:35
# @Author  : 蔍鸣霸霸
# @FileName: youwant.py
# @Software: PyCharm
# @Blog    ：只因你太美
import time

import pandas as pd
import requests
from openpyxl import Workbook



cookies = {
    'ASP.NET_SessionId': 'xmjzzvqmldz1vcatyxvpjir0',
    'Hm_lvt_a3f959ea0a0978d6e8f7e8dac01c39d9': '1678258605',
    'YOUWANTDATA': 'UserId=e6a157d283517188&Password=4d1dcbdc97c755d9de0b1ea8efe31ba3&ChildUserId=103dad732c906557&ClientId=98de212351ca49209d7db0e34e4fa714',
    '_data_chl': 'key=www.google.com',
    'Qs_lvt_466494': '1678258604%2C1678260458',
    'Hm_lpvt_a3f959ea0a0978d6e8f7e8dac01c39d9': '1678260481',
    'Qs_pv_466494': '3575732043029473000%2C1855987487373814300%2C3833573038655853600%2C1380647971442256000',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://www.youwant.cn',
    'Referer': 'https://www.youwant.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}


def get_data(city_code, city_s):
    wb = Workbook()
    ws = wb.active
    ws.append(['用户名', '粉丝数', '作品数', '平均点赞', '平均转发', '平均评论', '平均收藏', '账号类型', '友望指数'])
    url = f'https://api.youwant.cn/v1/blogger/search?pageIndex=1&pageSize=10&level1CategoryId=12&level2CategoryId=0&SortType=1&cityId={city_code}&type=-1&_=1678261008747'
    response = requests.get(url, headers=headers, cookies=cookies).json()
    # print(response)
    for city in city_s:
        city_list = str(response['Data']['ItemList'])
        # print(city_list)
        if str(city) in city_list:
            print(city)
            item_list = response['Data']['ItemList']
            for item in item_list:
                # 用户名
                user_name = item['NickName']
                # 粉丝数
                fans_count = item['FansCountDesc']
                # 作品数
                works_count = item['FeedsCountDesc']
                # 平均点赞
                avg_like = item['AvgLikeCountDesc']
                # 平均转发
                avg_forward = item['AvgForwardCountDesc']
                # 平均评论
                avg_comment = item['AvgCommentCountDesc']
                # 平均收藏
                avg_collect = item['AvgFavCountDesc']
                # 账号类型
                account_type = item['CategoryName']
                # 友望指数
                friend_index = item['GuaZhiShuDesc']
                ws.append([user_name, fans_count, works_count, avg_like, avg_forward, avg_comment, avg_collect,
                           account_type, friend_index])
                print(user_name, fans_count, works_count, avg_like, avg_forward, avg_comment, avg_collect, account_type,
                      friend_index)
            wb.save(rf'./data/{city}.xlsx')


if __name__ == '__main__':
    city_s = pd.read_excel(r'./data/城市.xlsx')['城市']
    for i in range(36, 378):
        get_data(i, city_s)
        time.sleep(2)


# level1CategoryId=12&level2CategoryId=0&SortType=1
# level1CategoryId=0&level2CategoryId=0&SortType=1