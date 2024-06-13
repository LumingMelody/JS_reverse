# -*- coding: utf-8 -*-
# @Time    : 2023/3/13 14:57
# @Author  : 蔍鸣霸霸
# @FileName: dy_rpc.py
# @Software: PyCharm
# @Blog    ：只因你太美
import json
import asyncio
import re
import time
import websockets
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.append(['live_data'])


async def check_permit(websocket):
    send_text = 'luming'
    await websocket.send(send_text)
    return True


async def recv_msg(websocket):
    while 1:
        recv_text = await websocket.recv()
        print(recv_text)
        ws.append([recv_text])
        wb.save(r'./data/live_data.xlsx')


async def main_logic(websocket, path):
    await check_permit(websocket)
    await recv_msg(websocket)


start_server = websockets.serve(main_logic, '127.0.0.1', 9999)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
#
# data = "{\"imUserDTO\":{\"userId\":\"484832608\",\"userName\":\"ARG779874884\",\"avatar\":\"https://www.dpfile.com/ugc/user/120/orange.png\",\"deviceId\":\"\",\"appId\":10,\"userType\":null,\"alias\":null},\"msgType\":5,\"chatRoomId\":309555,\"imMsgDTO\":{\"content\":null,\"snNo\":676485674,\"featureMap\":{},\"chatRoomUserNum\":7963,\"chatRoomClosed\":false,\"onlineCountNow\":\"279\",\"onlineCount\":\"7963\"},\"msgExtends\":\"null\",\"ts\":1687230669851}"
# pattern = re.compile(r'{"imUserDTO":{"userId":"(.*?)","userName":"(.*?)".*?},.*?onlineCountNow":"(.*?)","onlineCount":"(.*?)".*?,"ts":(.*?)}', re.S)
# match = pattern.search(data)
# if match:
#     user_id = match.group(1)
#     user_name = match.group(2)
#     online_count_now = match.group(3)
#     online_count = match.group(4)
#     ts = match.group(5)
#     timestamp = time.localtime(int(ts) / 1000)
#     post_time = time.strftime('%Y-%m-%d %H:%M:%S', timestamp)
# else:
#     print("未找到匹配项")
