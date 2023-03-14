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

wb = Workbook()
ws = wb.active
ws.append(
    ['文章作者', '作者主页', '文章标题', '文章内容', '文章链接', '文章点赞数', '文章评论数', '文章分享数', '文章收藏数',
     '文章发布时间'])

headers = {
    'authority': 'edith.xiaohongshu.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'xhsTrackerId=026c0cb3-a700-4cb3-8028-aa9250a459fb; xhsTrackerId.sig=sBicF6SeFKz1sG106f10CTLGxd1gBA1o3uVabWCNiEY; a1=186a0f1cf00cyprlnpc98qo6zobuu8jz9tm4aeaq030000818168; webId=8db5cbb3877e71dc815023bad3dcc9c8; gid=yYK08iyiWjj4yYK08iySi9d088SvUF1IUSjY6A8AlKulD4q877YVu0888YyYyKY8fdd84j22; gid.sign=z9YuhADLvkH9KOb6jOs4jijOMM4=; xhsTracker=url=explore&xhsshare=CopyLink; xhsTracker.sig=wmLdXV__wbETiz1qUgqoiY8swj2zGxC5B-xOV9HIhWg; webBuild=1.2.1; customerBeakerSessionId=c7b0ce65bf1ff687bdba186cb8121e0c6116590bgAJ9cQAoWBAAAABjdXN0b21lclVzZXJUeXBlcQFLAlgOAAAAX2NyZWF0aW9uX3RpbWVxAkdB2QH87cxqf1gJAAAAYXV0aFRva2VucQNYQQAAAGQ2MjM3ZTE1NmRhMDQ1MzViYTQ0ODhkOGMwOTU0MGVkLTljNGE2ZTE1NjIxYzRmOTY4ZmI3OTA4ZjFiMDBjYmE5cQRYAwAAAF9pZHEFWCAAAAAxODgyYWM1ODM0MmQ0MjU2OTJhMDVlODFhOWJiZGE2OXEGWA4AAABfYWNjZXNzZWRfdGltZXEHR0HZAfztzGp/WAYAAAB1c2VySWRxCFgYAAAANjI4NzAzOTNmNjgzZTMwMDAxMjgyMDZkcQl1Lg==; customerClientId=296354310261633; x-user-id-creator.xiaohongshu.com=62870393f683e3000128206d; access-token-creator.xiaohongshu.com=customer.ares.AT-1c2f5d30d2bd403b803d772cc6a2618e-33e23d08ee1f42ca8a9c2fd2bbc31efc; galaxy.creator.beaker.session.id=1678242743288047136108; extra_exp_ids=h5_230301_exp1,h5_1130_clt,ios_wx_launch_open_app_exp,h5_video_ui_exp3,wx_launch_open_app_duration_origin,ques_clt2; extra_exp_ids.sig=yi1oiDZ_OTBT0Y_iZlLv_doi507yh_p9E8YhpEcxTi8; xsecappid=xhs-pc-web; acw_tc=fe28e8aca20b9af9a2f2ffe8861c9a1d465ad0c12eda618f6c525bab23bd626e; web_session=040069768cba57210846c4563d364bcbfe6c30; websectiga=cffd9dcea65962b05ab048ac76962acee933d26157113bb213105a116241fa6c; sec_poison_id=4b205612-c63b-4d48-849e-473eba515cdf',
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
        result = re.findall(r'"prevRoute":"Empty","note":(.*?),"volume":', response.text)[0]
        note = json.loads(result)
        # print(note)
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
    wb.save('./data/red_book.xlsx')


async def main():
    tasks = []
    df = pd.read_excel(r'./urls.xlsx')
    urls = df['文章链接']
    for index, url in enumerate(urls):
        tasks.append(asyncio.create_task(get_red_book_data(url)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
