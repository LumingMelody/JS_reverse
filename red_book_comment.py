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

from red_book import register_webId

wb = Workbook()
ws = wb.active
ws.append(['昵称', '评论内容', '评论文章ID'])

headers = {
    'authority': 'edith.xiaohongshu.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    # "cookie": f"web_session=040069768cba57210846e50e10364bc14e67d7",
    'cookie': 'xhsTrackerId=026c0cb3-a700-4cb3-8028-aa9250a459fb; xhsTrackerId.sig=sBicF6SeFKz1sG106f10CTLGxd1gBA1o3uVabWCNiEY; a1=186a0f1cf00cyprlnpc98qo6zobuu8jz9tm4aeaq030000818168; webId=8db5cbb3877e71dc815023bad3dcc9c8; gid=yYK08iyiWjj4yYK08iySi9d088SvUF1IUSjY6A8AlKulD4q877YVu0888YyYyKY8fdd84j22; gid.sign=z9YuhADLvkH9KOb6jOs4jijOMM4=; customerClientId=296354310261633; x-user-id-creator.xiaohongshu.com=62870393f683e3000128206d; access-token-creator.xiaohongshu.com=customer.ares.AT-1c2f5d30d2bd403b803d772cc6a2618e-33e23d08ee1f42ca8a9c2fd2bbc31efc; x-user-id-pgy.xiaohongshu.com=607e4f9b2b9c54000132a33b; extra_exp_ids=yamcha_0327_exp,h5_1208_exp3,ques_clt2; extra_exp_ids.sig=ETM51AFqVyLPOioG2x0qNaEzMLVwrEIN37uTpfkLqxc; web_session=040069768cba5721084655c01a364bd035988c; xhsTracker=url=explore&searchengine=baidu; xhsTracker.sig=u1cFYHAwm89lKbFLL1Y8vp9JcskioXWTa56RKaAB2ys; xsecappid=xhs-pc-web; webBuild=2.0.3; acw_tc=50ebca4d9bc2ca1e01fd2859c0ff29fd80f96d9124ed698610ea77734d62b7e1; websectiga=634d3ad75ffb42a2ade2c5e1705a73c845837578aeb31ba0e442d75c648da36a; sec_poison_id=5e14eadf-1e06-4e2a-9aa2-7ebdac88d0a2',
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
