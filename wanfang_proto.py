# -*- coding: utf-8 -*-
# @Time    : 2023/3/17 15:58
# @Author  : 蔍鸣霸霸
# @FileName: wanfang_proto.py
# @Software: PyCharm
# @Blog    ：只因你太美
import pandas as pd
import requests

import s_pb2 as pb

data = {
    "searchType": "paper",
    "searchWord": "luming",
    "currentPage": 1,
    "pageSize": 20,
    "searchFilter": [
        0
    ],
    "searchSort": {
        "field": "",
        "order": 1
    },
    "searchScope": 0
}

url = 'https://s.wanfangdata.com.cn/SearchService.SearchService/search?'

headers = {
    'origin': 'https://s.wanfangdata.com.cn',
    'Content-Type': 'application/grpc-web+proto',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    'x-grpc-web': '1',
    'x-user-agent': 'grpc-web-javascript/0.1'
}



search_request = pb.SearchRequest()
search_request.commonrequest.searchType = "paper"
search_request.commonrequest.searchWord = 'lxlx'
search_request.commonrequest.searchScope = 0
search_request.commonrequest.currentPage = 1
search_request.commonrequest.pageSize = 20
search_request.commonrequest.searchFilter.append(0)

bytes_body = search_request.SerializeToString()

bytes_head = bytes([0, 0, 0, 0, len(bytes_body)])

resp = requests.post(url=url,data=bytes_head+bytes_body,headers=headers)
print(resp.text)