# -*- coding: utf-8 -*-
# @Time    : 2023/3/8 13:45
# @Author  : 蔍鸣霸霸
# @FileName: red_report_com_coll.py
# @Software: PyCharm
# @Blog    ：只因你太美
import asyncio
import json
import re
import time

from openpyxl import Workbook
import httpx
import pandas as pd

from red_book import register_session

wb = Workbook()
ws = wb.active
ws.append(
    ['文章作者', '作者主页', '文章标题', '文章内容', '文章链接', '文章点赞数', '文章评论数', '文章分享数', '文章收藏数',
     '文章发布时间'])


headers = {
    'authority': 'edith.xiaohongshu.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': f"web_session={register_session()}",
    'origin': 'https://www.xiaohongshu.com',
    'referer': 'https://www.xiaohongshu.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-b3-traceid': '61e0d1b7ceecaeed',
    # 'x-s': 'O6qksBci0g1CZ2ZvOlMCZ6qUZYsWZY1islqksBdv0j53',
    'x-t': '1678255137697',
}


async def get_red_book_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        print(response.text)
        result = re.findall(r'"prevRoute":"Empty","note":(.*?),"volume":', response.text)[0]
        note = json.loads(result)
        print(note)
        # 文章作者
        author = note['user']['nickname']
        # 作者主页
        author_url = f'https://www.xiaohongshu.com/user/profile/{note["user"]["userId"]}'
        # 文章标题
        title = note['title']
        # 文章内容
        desc = note['desc']
        # 文章链接
        note_id = note['noteId']
        note_url = f'https://www.xiaohongshu.com/explore/{note_id}'
        # 文章点赞数
        like_count = note['interactInfo']['likedCount']
        # 文章评论数
        comment_count = note['interactInfo']['commentCount']
        # 文章分享数
        share_count = note['interactInfo']['shareCount']
        # 文章收藏数
        collect_count = note['interactInfo']['collectedCount']
        # 文章发布时间
        publish_time = int(note['time']) / 1000
        post_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(publish_time))
        ws.append([author, author_url, title, desc, note_url, like_count, comment_count, share_count, collect_count,
                   post_time])
    wb.save('./data/red_book_23_05_05.xlsx')


async def main():
    tasks = []
    df = pd.read_excel(r'./long_urls.xlsx')
    urls = df['文章链接']
    for index, url in enumerate(urls):
        tasks.append(asyncio.create_task(get_red_book_data(url)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
