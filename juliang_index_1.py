# -*- coding: utf-8 -*-

import json
from selenium import webdriver
# import undetected_chromedriver as webdriver
# from undetected_chromedriver.options import ChromeOptions
from lxpy import copy_headers_dict
import base64
from Cryptodome.Cipher import AES
import ssl
from oceanengine_AES import decrypt_data
# ssl._create_default_https_context = ssl._create_unverified_context

h = copy_headers_dict('''
    accept: application/json, text/plain, */*
    accept-encoding: gzip, deflate, br
    accept-language: zh-CN,zh;q=0.9
    cache-control: no-cache
    content-length: 89
    content-type: application/json;charset=UTF-8
    cookie: i18next=zh; MONITOR_WEB_ID=75a85826-c1b9-49f2-b7f8-7a1a383b4dd6; x-jupiter-uuid=16327104466868524; Hm_lvt_c36ebf0e0753eda09586ef4fb80ea125=1632709872,1632710446; Hm_lpvt_c36ebf0e0753eda09586ef4fb80ea125=1632710446; tt_scid=4hsZnfHNAtmWGSi4MWUNz-N1DPpijAYZKyzkeKneA2n.ECIhOKPqYLGHBiH8H5zm15f6; s_v_web_id=verify_ku21n812_2kf7njXo_yptW_4Q86_BXNX_Y67hNBvJscUD; _csrf_token=R1pNiIx5y40wvC5reN0CybZa
    origin: https://trendinsight.oceanengine.com
    pragma: no-cache
    referer: https://trendinsight.oceanengine.com/arithmetic-index/analysis?keyword=lx
    sec-ch-ua: "Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"
    sec-ch-ua-mobile: ?0
    sec-ch-ua-platform: "Windows"
    sec-fetch-dest: empty
    sec-fetch-mode: cors
    sec-fetch-site: same-origin
    tea-uid: 6945252828761294374
    user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36
    ''')


class Browser():
    def __init__(self, **kwargs, ):
        self.debug = kwargs.get("debug", False)
        self.proxy = kwargs.get("proxy", None)
        self.api_url = kwargs.get("api_url", None)
        self.referrer = kwargs.get("referer", "https://trendinsight.oceanengine.com/")
        # TODO： update your executablePath
        self.executablePath = kwargs.get("executablePath", r"chromedriver.exe")

        args = kwargs.get("browser_args", [])
        options = kwargs.get("browser_options", {})

        if len(args) == 0:
            self.args = []
        else:
            self.args = args

        options = webdriver.ChromeOptions()
        # options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("log-level=2")
        options.add_argument("--lang=en-US")
        self.options = {
            "headless": True,
            "handleSIGINT": True,
            "handleSIGTERM": True,
            "handleSIGHUP": True,
        }

        if self.proxy is not None:
            if "@" in self.proxy:
                server_prefix = self.proxy.split("://")[0]
                address = self.proxy.split("@")[1]
                self.options["proxy"] = {
                    "server": server_prefix + "://" + address,
                    "username": self.proxy.split("://")[1].split(":")[0],
                    "password": self.proxy.split("://")[1].split("@")[0].split(":")[1],
                }
            else:
                self.options["proxy"] = {"server": self.proxy}

        if self.executablePath is not None:
            self.options["executablePath"] = self.executablePath

        self.browser = webdriver.Chrome(executable_path=self.executablePath, chrome_options=options)
        self.browser.get('https://trendinsight.oceanengine.com/arithmetic-index')

    def signature(self, keyword, start_date, end_date):
        sign_url = self.browser.execute_script('''
                    function queryData(url) {
                       var p = new Promise(function(resolve,reject) {
                           var e={"url":"https://trendinsight.oceanengine.com/api/open/index/get_multi_keyword_hot_trend",
                                    "method":"POST",
                                    "data" : '{"keyword_list": ["%s"],"start_date": "%s","end_date": "%s","app_name": "aweme"}'};
                            var h = new XMLHttpRequest;h.open(e.method, e.url, true);
                            h.setRequestHeader("accept","application/json, text/plain, */*");  
                            h.setRequestHeader("content-type","application/json;charset=UTF-8");
                            h.setRequestHeader("tea-uid","7054893410171930123");
                            h.onreadystatechange =function() {
                                 if(h.readyState != 4) return;
                                 if(h.readyState === 4 && h.status  ===200) {
                                    resolve(h.responseText);
                                 } else {
                                  }
                            };
                            h.send(e.data);
                            });
                            return p;
                        }
                    var p1 = queryData('lx');
                    res = Promise.all([p1]).then(function(result){
                    return result
                    })
                    return res;
        ''' % (keyword, start_date, end_date))
        '''
        let e={"url":"https://trendinsight.oceanengine.com/api/open/index/get_multi_keyword_hot_trend",
                                "method":"POST",
                                "data" : '{"keyword_list":["lx"],"start_date":"20220430","end_date":"20220530","app_name":"aweme"}'};
        var h = new XMLHttpRequest;h.open(e.method, e.url, true);
        h.setRequestHeader("accept","application/json, text/plain, */*");
        h.setRequestHeader("content-type","application/json;charset=UTF-8");
        h.setRequestHeader("tea-uid","7054893410171930123");
                h.onreadystatechange=function(){
                    if (h.status===200){
                       console.log(h.responseText)
                       console.log(h.responseURL)
                    }
                }
        h.send(e.data);
        '''
        return sign_url[0]

    def close(self):
        self.browser.close()
        self.browser.quit()


def get_data(keyword, start_date, end_date):
    data = '{"keyword_list": ["%s"],"start_date": "%s","end_date": "%s","app_name": "aweme"}' % (
    keyword, start_date, end_date)
    data = browser.signature(keyword=keyword, start_date=start_date, end_date=end_date)
    doc = json.loads(data)['data']
    return doc


# AES-128
# def decrtptlx(String):
#     iv = "amlheW91LHFpYW53".encode(encoding='utf-8')
#     key = 'anN2bXA2NjYsamlh'.encode(encoding='utf-8')
#     cryptor = AES.new(key=key, mode=AES.MODE_CFB, IV=iv, segment_size=128)
#     decode = base64.b64decode(String)
#     plain_text = cryptor.decrypt(decode)
#     print(plain_text)
#     return plain_text


browser = Browser()
# test
result = decrypt_data(get_data(keyword='lx', start_date="20210826", end_date="20210926"))
print(result)
browser.close()
