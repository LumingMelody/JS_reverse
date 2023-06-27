import time

import pandas as pd
from openpyxl import Workbook
import requests, json
import execjs

wb = Workbook()
ws = wb.active
ws.append(
    ['用户名', '用户id', '文章链接', '文章标题', '文章内容', '文章点赞数', '文章评论数', '文章收藏数', '文章分享数',
     '文章发布时间'])


def feed(source_note_id, web_session, a1):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "cookie": f"a1={a1}; web_session={web_session};",
        "origin": "https://www.xiaohongshu.com",
        "pragma": "no-cache",
        "referer": "https://www.xiaohongshu.com/",
        "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "x-b3-traceid": "a31fffc0ee4f5d8f",
        "x-s-common": "",
    }
    data = {"source_note_id": source_note_id}
    exc = execjs.compile(open('./js_signature/xs20230531.js', 'r', encoding='utf-8').read())
    xs_xt = exc.call('get_xs', '/api/sns/web/v1/feed', data, a1)
    xs_xt['X-t'] = str(xs_xt['X-t'])
    print(xs_xt)
    headers.update(xs_xt)
    feed = 'https://edith.xiaohongshu.com/api/sns/web/v1/feed'
    resp = requests.post(url=feed, data=json.dumps(data, separators=(",", ":")), headers=headers).json()
    print(resp['data']['items'][0])
    result = resp['data']['items'][0]['note_card']
    nickname = result['user']['nickname']
    user_id = result['user']['user_id']
    note_url = f"https://www.xiaohongshu.com/explore/{source_note_id}"
    title = result['title']
    desc = result['desc']
    liked_count = result['interact_info']['liked_count']
    comment_count = result['interact_info']['comment_count']
    collected_count = result['interact_info']['collected_count']
    share_count = result['interact_info']['share_count']
    ts = result['time']
    post_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(ts) / 1000))
    print(nickname, user_id, note_url, title, desc, liked_count, comment_count, collected_count, share_count,
          post_time)
    ws.append([nickname, user_id, note_url, title, desc, liked_count, comment_count, collected_count, share_count,
               post_time])
    wb.save('./data/家电_.xlsx')


if __name__ == '__main__':
    web_session = "0400697973c8d5d1f5a13633af364b9673ad1f"
    a1 = "186a0f1cf00cyprlnpc98qo6zobuu8jz9tm4aeaq030000818168"
    # source_note_id = "632528900000000018015b2d"
    df = pd.read_excel('./data/家电.xlsx')
    for note_id in df['note_id']:
        feed(note_id, web_session, a1)
        time.sleep(3)
