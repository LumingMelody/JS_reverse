import requests
import execjs
import random


def register_Id(c=32):
    s = "abcdef0123456789"
    webId = ''
    for i in range(c):
        webId += random.choice(s)
    return webId


# def register_session():
#     url = 'https://edith.xiaohongshu.com/api/sns/web/v1/login/activate'
#     headers = {
#         "accept": "application/json, text/plain, */*",
#         "accept-encoding": "gzip, deflate, br",
#         "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
#         "cache-control": "no-cache",
#         "content-type": "application/json;charset=UTF-8",
#         "cookie": f"a1=1879883dcb2xqzqkj7hhp1wtwys56f4jl7omndiyd50000102326; webId={register_Id()}; gid=yYWjYYqdyd1jyYWjYYqfSWf3DJCAuATVWxxUlvfyE9EvM6282Ki4VI888y8JqJK84SqKdfJq; gid.sign=IaDqCp2Q97+mPBsh9MZLtE69xs4=",
#         "origin": "https://www.xiaohongshu.com",
#         "pragma": "no-cache",
#         "referer": "https://www.xiaohongshu.com/",
#         "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
#         "sec-ch-ua-mobile": "?0",
#         "sec-ch-ua-platform": "\"Windows\"",
#         "sec-fetch-dest": "empty",
#         "sec-fetch-mode": "cors",
#         "sec-fetch-site": "same-site",
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
#         "x-b3-traceid": "453f324415a7086f",
#         "x-s-common": "2UQAPsHC+aIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1PjhIHjIj2eHjwjQgynEDJ74AHjIj2ePjwjQhyoPTqBPT49pjHjIj2ecjwjHUN0Z1+UHVHdWMH0ijP/W7w/WhP9z0G0Qhqgkly9i7yBYIPg4F47SA+/8f+BkV+9RTJfzk2ncMPeZIPerIP0PU+jHVHdW9H0il+0WlweDlPerEPerUNsQh+UHCHDRd4A8A8AzpP/Q7c0mdzfSA8MzgqMSl40bd/FQOcd4sq9lOp/mxqF4A8FGAHjIj2eWjwjQQPAYUaBzdq9k6qB4Q4fpA8b878FSet9RQzLlTcSiM8/+n4MYP8F8LagY/P9Ql4FpUzfpS2BcI8nT1GFbC/L88JdbFyrSiafp/JDMra7pFLDDAa7+8J7QgabmFz7Qjp0mcwp4fanD68p40+fp8qgzELLbILrDA+9p3JpHlLLI3+LSk+d+DJfRAyfRL+gSl4bYlqg48qDQlJFShtUTozBD6qM8FyFShPo+h4g4U+obFyLS3qd4QyaRAy9+0PFSe/B8QPFRSPopFJeHIzbkA/epSzb+t8nkn4AmQynpS2b87/sTc4BRUqgziLrSN8gY8wBRQcMHlaLpUL94n4FQoqgzaagYbGnpr8Bpn4g4xaLPIqAbl4BEQy7mNanYgnfpSP7+88Fq9GMLMqMSl4okYzBzS8dklPgkDN9pgpF8wagWM8n8M4sRQzLES8SmFcgQCqfYOJM8oag8d8nSl4oL6nn4S2BklJLS3/o4QyLzcz9bTyDS9yBF3a/WhanSC4LQn49lQ4D4B+Bp98Lz/+9Ll4gzeaLP7qFz0O/FjNsQhwaHCP/L9Per9+/cANsQhP/Zjw0rIKc==",
#         "x-s": "Ogw6sg4U12wB0gFisgTWsYqv1gOBOBwBslOU0jsGsgF3",
#         "x-t": "1681891019012"
#     }
#     session = requests.post(url, data='{}', headers=headers).json()['data']['session']
#     return session

def register_session():
    headers = {
        'authority': 'edith.xiaohongshu.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'cookie': f'a1=186a0f1cf00cyprlnpc98qo6zobuu8jz9tm4aeaq030000818168; webId={register_Id()}; gid=yYK08iyiWjj4yYK08iySi9d088SvUF1IUSjY6A8AlKulD4q877YVu0888YyYyKY8fdd84j22; gid.sign=z9YuhADLvkH9KOb6jOs4jijOMM4=; customerClientId=296354310261633; x-user-id-creator.xiaohongshu.com=62870393f683e3000128206d; access-token-creator.xiaohongshu.com=customer.ares.AT-1c2f5d30d2bd403b803d772cc6a2618e-33e23d08ee1f42ca8a9c2fd2bbc31efc; x-user-id-pgy.xiaohongshu.com=607e4f9b2b9c54000132a33b; xsecappid=xhs-pc-web; extra_exp_ids=yamcha_0327_exp,h5_1208_exp3,ques_clt2; extra_exp_ids.sig=ETM51AFqVyLPOioG2x0qNaEzMLVwrEIN37uTpfkLqxc; xhsTracker=url=explore&xhsshare=CopyLink; xhsTracker.sig=wmLdXV__wbETiz1qUgqoiY8swj2zGxC5B-xOV9HIhWg; websectiga=6169c1e84f393779a5f7de7303038f3b47a78e47be716e7bec57ccce17d45f99; sec_poison_id=aa05fe5e-1162-450a-b08b-fccd726c96f2; acw_tc=9083d495d862ce019e4998c2bc197bfd93fa9cca5a03992570f8f3995b3d5a03; webBuild=2.3.0; web_session=',
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


def feed(source_note_id):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
        "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "cookie": f"web_session={register_session()}",  # web_session和当前IP或者环境绑定，重新注册后浏览器中的ID也会更新
        "origin": "https://www.xiaohongshu.com",
        "pragma": "no-cache",
        "referer": "https://www.xiaohongshu.com/",
        "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "x-s": "1lqJsBVUOjsiO6dk1BspOg9G16O6sgAWslOJ1gkvOgF3",
        "x-t": "1675387207946"
    }
    with open('./js_signature/xhs_xt.js', 'r', encoding='utf-8') as f:
        js = f.read()
    crt = execjs.compile(js)
    data = '{"source_note_id":"%s"}' % source_note_id
    xs_xt = crt.call('sign', '/api/sns/web/v1/feed', {"source_note_id": "%s" % source_note_id})
    xs_xt['X-t'] = str(xs_xt['X-t'])

    headers.update(xs_xt)
    feed = 'https://edith.xiaohongshu.com/api/sns/web/v1/feed'
    print(requests.post(url=feed, data=data, headers=headers).text)


if __name__ == '__main__':
    # print(register_session())
    feed("63cf8afe000000001f023d49")
