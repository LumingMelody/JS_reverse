# -*- coding: utf-8 -*-
# @Time    : 2023/3/8 18:27
# @Author  : 蔍鸣霸霸
# @FileName: red_book_keyword.py
# @Software: PyCharm
# @Blog    ：只因你太美
import requests
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.append(['标题', '内容'])


# 最热 popularity_descending
# 最新 time_descending
# 综合 general
def get_data(key_word, page):
    url = f'http://whosecard.com:8081/api/xiaohongshu/search/notes/v1?key=f1211ee24a26dfefc195b3ae9da1dd79cdc3019d39d738654c46911d&keyword={key_word}&sort=popularity_descending&page={page}'
    print(url)
    resp = requests.get(url).json()
    items = resp['result']['data']['items']
    for item in items:
        print(item)
        if item.get('note'):
            note = item['note']
            title = note['title']
            desc = note['desc']
            detail = title + desc
            # ws.append([title, desc])
            ws.append([detail])
    wb.save(rf'./data/小红书_{key_word}.xlsx')


if __name__ == '__main__':
    key_word_list = ["太湖"]
    for key_word in key_word_list:
        for i in range(1, 6):
            get_data(key_word, i)
