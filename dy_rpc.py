# -*- coding: utf-8 -*-
# @Time    : 2023/3/13 14:57
# @Author  : 蔍鸣霸霸
# @FileName: dy_rpc.py
# @Software: PyCharm
# @Blog    ：只因你太美

import asyncio
import websockets


async def check_permit(websocket):
    send_text = 'luming'
    await websocket.send(send_text)
    return True


async def recv_msg(websocket):
    while 1:
        recv_text = await websocket.recv()
        print(recv_text)


async def main_logic(websocket, path):
    await check_permit(websocket)
    await recv_msg(websocket)


start_server = websockets.serve(main_logic, '127.0.0.1', 9999)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
