# -*- coding: utf-8 -*-
# @Time    : 2023/4/27 14:21
# @Author  : 蔍鸣霸霸
# @FileName: xhs_webssion.py
# @Software: PyCharm
# @Blog    ：只因你太美
import json

import requests
import random


def register_webId():
    s = "abcdef0123456789"
    webId = ''
    for i in range(32):
        webId += random.choice(s)
    return webId


def register_session():
    headers = {
        'authority': 'edith.xiaohongshu.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'cookie': 'xhsTrackerId=026c0cb3-a700-4cb3-8028-aa9250a459fb; xhsTrackerId.sig=sBicF6SeFKz1sG106f10CTLGxd1gBA1o3uVabWCNiEY; a1=186a0f1cf00cyprlnpc98qo6zobuu8jz9tm4aeaq030000818168; webId=8db5cbb3877e71dc815023bad3dcc9c8; gid=yYK08iyiWjj4yYK08iySi9d088SvUF1IUSjY6A8AlKulD4q877YVu0888YyYyKY8fdd84j22; gid.sign=z9YuhADLvkH9KOb6jOs4jijOMM4=; customerClientId=296354310261633; x-user-id-creator.xiaohongshu.com=62870393f683e3000128206d; access-token-creator.xiaohongshu.com=customer.ares.AT-1c2f5d30d2bd403b803d772cc6a2618e-33e23d08ee1f42ca8a9c2fd2bbc31efc; x-user-id-pgy.xiaohongshu.com=607e4f9b2b9c54000132a33b; xsecappid=xhs-pc-web; extra_exp_ids=yamcha_0327_exp,h5_1208_exp3,ques_clt2; extra_exp_ids.sig=ETM51AFqVyLPOioG2x0qNaEzMLVwrEIN37uTpfkLqxc; xhsTracker=url=explore&xhsshare=CopyLink; xhsTracker.sig=wmLdXV__wbETiz1qUgqoiY8swj2zGxC5B-xOV9HIhWg; websectiga=6169c1e84f393779a5f7de7303038f3b47a78e47be716e7bec57ccce17d45f99; sec_poison_id=aa05fe5e-1162-450a-b08b-fccd726c96f2; acw_tc=9083d495d862ce019e4998c2bc197bfd93fa9cca5a03992570f8f3995b3d5a03; webBuild=2.3.0; web_session=',
        'origin': 'https://www.xiaohongshu.com',
        'pragma': 'no-cache',
        'referer': 'https://www.xiaohongshu.com/',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'x-b3-traceid': '2d87a55221f73cce',
        'x-s': 'sj4k0g1psBOv1gZJ16wkOYMpsg9+O6sWsgAiZ2FGZgM3',
        'x-s-common': '2UQAPsHCPUIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1PjhIHjIj2eHjwjQ+GnPW/MPjNsQhPUHCHdYiqUMIGUM78nHjNsQh+sHCH0H1PUhIHjIj2eLjwjHlwe8YPBGlG9GIPB+EqoQVJdm0w/YlJA8CJ9QM4/Yx20SFJ/zY8nblPePIPeZIwerhP/GhHjIj2eGjw0r9weHM+AqFPeLE+/ZVHdW7H0ijq9iFyAmdPgmAcDR9Pn4ya0r949TOnLMIq9qEtFu9qM4A8Fbkn0QBzMkd//PjNsQhwsHCHDDAwoQH8B4AyfRI8FS98g+Dpd4daLP3JFSb/BMsn0pSPM87nrldzSzQ2bPAGdb7zgQB8nph8emSy9E0cgk+zSS1qgzianYt8Lz1/LzN4gzaa/+NqMS6qS4HLozoqfQnPbZEp98QyaRSp9P98pSl4oSzcgmca/P78nTTL0bz/sVManD9q9z1J7+xJMcM2gbFnobl4MSUcdb6agW3tF4ryaRApdz3agWIq7YM47HFqgzkanTU4FSkN7+3G9PAaL+P8DDA/9LI4gzVP0mrnd+P+nprLFkSyS87PrSk8nphpd4PtMmFJ7Ql4BW3JrbSy9Mg+rSht9SQyoQa2S878FTc4bSQPMbcJ7QN8/8l4BYQ2sRA+S8FJFSk/nRQynYSJfG98p+DqgYU8d8AydpFa7Qy89pfG7HE898N8pS0Lo+Q2B4SL7pFqrSb89pDqgzVqSSyJbbD/BEQ2epAP7bFLfE0+9pn8Dq3anT04FSkaocFPBQ+ag8iqgz/wB4QynSfqb87cLSeab8tJA+SL7mS8nTc4b8Q2e+SPBzOqM40O/FjNsQhwaHCP0HMPerI+0PVHdWlPsHCP/P7Kc==',
        'x-t': '1682577405950',
    }

    data = '{}'

    response = requests.post('https://edith.xiaohongshu.com/api/sns/web/v1/login/activate', headers=headers, data=data)
    print(response.json())
    session = response.json()['data']['session']
    return session


if __name__ == '__main__':
    xhs_session = register_session()
    print(xhs_session)
