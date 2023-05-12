# -*- coding: utf-8 -*-
# @Time    : 2023/5/8 10:28
# @Author  : 蔍鸣霸霸
# @FileName: red_book_search.py
# @Software: PyCharm
# @Blog    ：只因你太美
import json

import requests
from red_book import register_session
from xhs import help

headers = {
    'authority': 'edith.xiaohongshu.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'cookie': 'xhsTrackerId=026c0cb3-a700-4cb3-8028-aa9250a459fb; xhsTrackerId.sig=sBicF6SeFKz1sG106f10CTLGxd1gBA1o3uVabWCNiEY; a1=186a0f1cf00cyprlnpc98qo6zobuu8jz9tm4aeaq030000818168; webId=8db5cbb3877e71dc815023bad3dcc9c8; gid=yYK08iyiWjj4yYK08iySi9d088SvUF1IUSjY6A8AlKulD4q877YVu0888YyYyKY8fdd84j22; gid.sign=z9YuhADLvkH9KOb6jOs4jijOMM4=; customerClientId=296354310261633; x-user-id-creator.xiaohongshu.com=62870393f683e3000128206d; access-token-creator.xiaohongshu.com=customer.ares.AT-1c2f5d30d2bd403b803d772cc6a2618e-33e23d08ee1f42ca8a9c2fd2bbc31efc; x-user-id-pgy.xiaohongshu.com=607e4f9b2b9c54000132a33b; xsecappid=xhs-pc-web; xhsTracker=url=explore&xhsshare=CopyLink; xhsTracker.sig=wmLdXV__wbETiz1qUgqoiY8swj2zGxC5B-xOV9HIhWg; web_session=040069768cba572108467f537f364b393aa2f6; webBuild=2.3.2; extra_exp_ids=yamcha_0327_exp,h5_1208_exp3,ques_clt2; extra_exp_ids.sig=ETM51AFqVyLPOioG2x0qNaEzMLVwrEIN37uTpfkLqxc; websectiga=634d3ad75ffb42a2ade2c5e1705a73c845837578aeb31ba0e442d75c648da36a; sec_poison_id=57b18e09-0f14-4aad-ac47-000a0d3a9f30; acw_tc=7d758bd20e5f80ae53f175968db5e198c4bb5c38ae424b7e646675eef4b45166',
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
    'x-b3-traceid': 'efae557ebc30a0f5',
    'x-s': 'ZjUvZYsWsYaB1BkUsBFlsjU6OjsC0gVU1lkBZB1Csj53',
    'x-s-common': '2UQAPsHCPUIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1PjhIHjIj2eHjwjQ+GnPW/MPjNsQhPUHCHdYiqUMIGUM78nHjNsQh+sHCH0H1PUhUHjIj2eLjwjHlwe8YPBGlG9GIPB+EqoQVJdm0w/YlJA8CJ9QM4/Yx20SFJ/zY8nblPePIPeZIwerhP/GhHjIj2eGjw0r9wePMP/HMw/WUw/PVHdW7H0ijnfkp4Sk8qM4AnnbsPLQ3pg+szflAySL9/9kAcAmdpSLlJBTsnDHlc7+x+/PjNsQhwsHCHDDAwoQH8B4AyfRI8FS98g+Dpd4daLP3JFSb/BMsn0pSPM87nrldzSzQ2bPAGdb7zgQB8nph8emSy9E0cgk+zSS1qgzianYt8p+1/LzN4gzaa/+NqMS6qS4HLozoqfQnPbZEp98QyaRSp9P98pSl4oSzcgmca/P78nTTL0bz/sVManD9q9z1J7+xJMcM2gbFnobl4MSUcdb6agW3tF4ryaRApdz3agWIq7YM47HFqgzkanTU4FSkN7+3G9PAaL+P8DDA/9LI4gzVP0mrnd+P+nprLFkSyS87PrSk8nphpd4PtMmFJ7Ql4BY7204Sy9Mg+rSht9SQyoQa2S878FTc4bSQPMbcJ7QN8/8l4BYQ2sRA+S8FJFSk/nRQynYSJfG98p+DqgYU8d8AydpFa7Qy89pfG7HE898N8pS0Lo+Q2sRSL7pFNFSb8npDLozbJ9lQcgzD/BEQ2epAP7bFLfE0+9pn8Dq3anT04FSkaocFPBQ+ag8iqgz/wB4QynSfqb87cLSeab8tJA+SL7mS8nTc4b8Q2e+SPBkHOaHVHdWEH0iTweWEweH9+0LENsQhP/Zjw0HFKc==',
    'x-t': '1683512598293',
}


def get_data(page_num):
    data = '{"keyword":"苏州","page":3,"page_size":20,"search_id":"2bmv36ul8q5x2bjbldtev","sort":"general","note_type":0}'
    data = json.loads(data)
    sign = help.sign('/api/sns/web/v1/search/notes', data, a1="186a0f1cf00cyprlnpc98qo6zobuu8jz9tm4aeaq030000818168",
                     b1="I38rHdgsjopgIvesdVwgIC+oIELmBZ5e3VwXLgFTIxS3bqwErFeexd0ekncAzMFYnqthIhJeSBMDKutRI3KsYorWHPtGrbV0P9WfIi/eWc6eYqtyQApPI37ekmR1QL+5Ii6sdnosjoT5yqtXqqwYrBqoIx++GDi/sVtkIx0sxuwr4qtiIkrwIi/skcc3ICLfI3Oe0utl20DZsL5eDSJejVw0IieexVwL+PtorqthwzAekmW4Ix+iIhrRzVwgKPtYI3QPorKe6qthIx/s6VtoIiMoIihenf6eSdqxrfvsjutKrZgefcr9gfKeYcPsIx/eSut/IEKefPtIbYWMNgLnIx5s3qtRnc7eVfG+IkcwIiHt40bMIvhqtS8gIiifpVwAICHVJo3eSpeekPtVIx3e0jH=")
    print(type(data))
    data['page'] = page_num
    headers['x-s'] = sign['x-s']
    headers['x-t'] = sign['x-t']
    headers['x-s-common'] = sign['x-s-common']
    data = json.dumps(data)
    response = requests.post('https://edith.xiaohongshu.com/api/sns/web/v1/search/notes', headers=headers,
                             data=data.encode('utf-8'))
    print(response.json())


if __name__ == '__main__':
    for i in range(1, 3):
        get_data(i)
