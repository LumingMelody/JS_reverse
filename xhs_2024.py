import json
import os
import re
import execjs
import requests

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
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
}


def getXs(cookie, api, data):
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, "./js_signature/xhs.js")
    with open(file_path, 'r', encoding='utf-8') as f:
        jstext = f.read()

    ctx = execjs.compile(jstext)

    match = re.search(r'a1=([^;]+)', cookie)
    a1 = ""
    if match:
        a1 = match.group(1)
    else:
        print("关键参数a1获取失败，请检查你的cookie")
        return ""
    print(api, data, a1)
    result = ctx.call("get_xs", api, data, a1)
    return result


def sentRequest(host, api, data, cookie):
    print(cookie, api, data)
    xs_xt = getXs(cookie, api, data)
    print(xs_xt)
    headers['cookie'] = cookie
    headers['X-s'] = xs_xt['X-s']
    headers['X-t'] = str(xs_xt['X-t'])

    url = host + api

    return requests.post(url=url, data=json.dumps(data, separators=(",", ":")), headers=headers)


def DoApi(param, cookie):
    api = '/api/sns/web/v1/feed'
    host = 'https://edith.xiaohongshu.com'
    data = param

    return sentRequest(host, api, data, cookie)


if __name__ == '__main__':

    cookie = "abRequestId=4c878db8-987e-5f31-8ef7-e8f9341402a1; a1=18f5de8cc89qvnfgyv14fp9o2wtl022cf43vms20930000249199; webId=f58b4c7a0fee41b97597a5adc1ee2b46; gid=yYi2d8Jy0diyyYi2fdYSS4MJYjAhIikvhy4iq8jUjlJE9hq818JJS6888J4jyjj8JYYSqW8J; customerClientId=446313658831135; x-user-id-pgy.xiaohongshu.com=5c219d1b000000000703d14b; web_session=0400697824b304216a0bb7ea60344b1bf99bdf; customer-sso-sid=665d648d480000000000000ab7e80f457d04c312; webBuild=4.20.1; xsecappid=xhs-pc-web; acw_tc=38fd301472f7ee3e041d2cad2b3e39bc462eacf735d342c0723d350481e4bdd3; customerClientId=709653815878651"  # put your cookie here

    param = {"source_note_id": "664f35ae000000000f00c945", "image_formats": ["jpg", "webp", "avif"],
             "extra": {"need_body_topic": "1"}}

    response = DoApi(param, cookie)
    if response.status_code == 200:
        print("Request successful:")
        print(response.json())
    else:
        print("POST request failed. Status code:", response.status_code)
        print(response.text)
