import loguru
import requests
import re
import execjs
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://www.nmpa.gov.cn/datasearch/home-index.html"
response = requests.get(url, headers=headers)
NfBCSins2OywO = response.cookies.get('NfBCSins2OywO')
acw_tc = response.cookies.get('acw_tc')
# print(response.content.decode('utf-8'))
arg1 = re.findall('content="(.*?)" r="',response.text)[0]
arg2 = re.findall("t\" r='m'>(.*?)</script><script ty",response.text)[0]
# print(arg1, arg2)
jscode = open('./yjj.js',encoding='utf-8').read().replace('arg1_content',arg1).replace('"arg2_js"',arg2)
NfBCSins2OywP = execjs.compile(jscode).call('get_cookie')
print(NfBCSins2OywP)
wp = NfBCSins2OywP.split('wP=')[1].split('; path=/')[0]
cookies = {
    "acw_tc": acw_tc,
    "NfBCSins2OywO": NfBCSins2OywO,
    "NfBCSins2OywP": wp,
    "STEP_TIPS_INDEX": "true",
    "token": "",
    "STEP_TIPS_RESULT": "true",
}
url = "https://www.nmpa.gov.cn/datasearch/home-index.html"
res = requests.get(url, headers=headers, cookies=cookies)
loguru.logger.info(res.content.decode('utf-8'))