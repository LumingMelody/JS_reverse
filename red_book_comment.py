# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 11:48
# @Author  : 蔍鸣霸霸
# @FileName: red_book_comment.py
# @Software: PyCharm
# @Blog    ：只因你太美
import time

import execjs
import requests
from openpyxl import Workbook


wb = Workbook()
ws = wb.active
ws.append(['昵称', '评论内容', '评论文章ID'])

headers = {
    'authority': 'edith.xiaohongshu.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    "cookie": f"web_session=040069768cba57210846d8e368364b9520f042",
    'origin': 'https://www.xiaohongshu.com',
    'referer': 'https://www.xiaohongshu.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-b3-traceid': '9d51ed8e9b7bd237',
    'x-s': 'sj4vs2MCOjTpZ2Mi1g9Ksis+021LOjqk16Oks2sb1lT3',
    'x-t': '1678333739647',
}


def get_xs(source_note_id, cursor=None):
    if cursor is None:
        cursor = ''
    with open('js_signature/xhs_xt.js', 'r', encoding='utf-8') as f:
        js = f.read()
    crt = execjs.compile(js)
    xs_xt = crt.call('sign', f'/api/sns/web/v2/comment/page?note_id={source_note_id}&cursor={cursor}')
    xs_xt['X-t'] = str(xs_xt['X-t'])
    headers.update(xs_xt)


def get_comment(source_note_id):
    get_xs(source_note_id)
    response = requests.get(
        f'https://edith.xiaohongshu.com/api/sns/web/v2/comment/page?note_id={source_note_id}&cursor=',
        headers=headers).json()
    print(response)
    while response['data']['has_more']:
        comments = response['data']['comments']
        for comment in comments:
            nick_name = comment['user_info']['nickname']
            content = comment['content']
            note_id = comment['note_id']
            ws.append([nick_name, content, note_id])
            print(nick_name, content, note_id)
        cursor = response['data']['cursor']
        get_xs(source_note_id, cursor)
        response = requests.get(
            f'https://edith.xiaohongshu.com/api/sns/web/v2/comment/page?note_id={source_note_id}&cursor={cursor}',
            headers=headers).json()
        print(response)
        wb.save(r'./data/red_book_comment.xlsx')
        time.sleep(2)


# /api/sns/web/v2/comment/page?note_id=640070c90000000013001b92&cursor=64084ec5000000000b0300e6
# /api/sns/web/v2/comment/page?note_id=640070c90000000013001b92&cursor=64084ec5000000000b0300e6
if __name__ == '__main__':
    get_comment('640070c90000000013001b92')
