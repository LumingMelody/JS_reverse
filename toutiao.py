# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 17:02
# @Author  : 蔍鸣霸霸
# @FileName: toutiao.py
# @Software: PyCharm
# @Blog    ：只因你太美
import execjs
import requests

headers = {
    'authority': 'www.toutiao.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '__ac_nonce=064099f5100040e7ade67; __ac_signature=_02B4Z6wo00f01P5E-7wAAIDDapKgsAfOk8D-ZP8AAFue88; tt_webid=7199889069449659959; ttcid=93b82c558e7848e796cda84d30b7745592; local_city_cache=%E8%8B%8F%E5%B7%9E; csrftoken=4fd2c47b001c58bd5bac7153d5c69de3; s_v_web_id=verify_lf0vkovr_OLbpu528_lwQs_4wFP_Ai0l_pM7A6uiIpEM9; _ga=GA1.1.1148734291.1678352219; ttwid=1%7CbMOyyaWy9rzXLSyJ7HtFZKprrCjavHwDT6za9oE5xOE%7C1678352510%7Ce639c1546bc62cc8af87cb7403ee5e886285ba2e68502717dd28b54ae4a71df2; tt_scid=g819p1r0Nr0cz8Hds9gb-ZleijjiZSjkRf5jeq2VAixjTjcsKG1t5-AeIcG4SE5N2436; _ga_QEHZPBE5HH=GS1.1.1678352218.1.1.1678352517.0.0.0',
    'referer': 'https://www.toutiao.com/c/user/token/MS4wLjABAAAAaezOXkHVr0_i2JvWXprb4zLGpRInnKStptFm5WsXHKU/?source=feed&log_from=4d36a32f09a23_1658889632302&tab=article&wid=1678352210934',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}


def get_data():
    url = f'https://www.toutiao.com/api/pc/list/user/feed?category=pc_profile_article&token=MS4wLjABAAAAaezOXkHVr0_i2JvWXprb4zLGpRInnKStptFm5WsXHKU&max_behot_time=0&aid=24&app_name=toutiao_web&_signature=_02B4Z6wo00901jX7xswAAIDBoS2dwKwE.CY138JAAOmFBlrVvdYYaavNGiUZREHfSlDHQ-tGNOiTj80g8jbG-5JTFFcyjtQh5fvKgSWNGN.OQiteat6QTmwOdY72nzDzCusvav9BGM11zF1506'
    response = requests.get(url, headers=headers).json()
    # print(response)
    max_bottom_time = response['next']['max_behot_time']
    data = f'/api/pc/list/feed?category=pc_profile_article&token=MS4wLjABAAAAaezOXkHVr0_i2JvWXprb4zLGpRInnKStptFm5WsXHKU&max_behot_time={max_bottom_time}&aid=24&app_name=toutiao_web'
    with open('./js_signature/todays_signature.js', 'r', encoding='utf-8') as f:
        js = f.read()
    sign = execjs.compile(js).call('get_sign', data)
    # print(sign)
    next_url = f'https://www.toutiao.com{data}&_signature={sign}'
    print(next_url)


if __name__ == '__main__':
    get_data()
