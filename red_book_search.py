# -*- coding: utf-8 -*-
# @Time    : 2023/5/8 10:28
# @Author  : 蔍鸣霸霸
# @FileName: red_book_search.py
# @Software: PyCharm
# @Blog    ：只因你太美
from time import sleep
from xhs import FeedType, XhsClient
from playwright.sync_api import sync_playwright


def get_context_page(playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=True)
    browser_context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    )
    browser_context.add_init_script(path="stealth.min.js")
    context_page = browser_context.new_page()
    return browser_context, context_page


playwright = sync_playwright().start()
browser_context, context_page = get_context_page(playwright)

cookie = "please get cookie in website"


def sign(uri, data=None, a1="", web_session=""):
    context_page.goto("https://www.xiaohongshu.com")
    cookie_list = browser_context.cookies()
    web_session_cookie = list(filter(lambda cookie: cookie["name"] == "web_session", cookie_list))
    if not web_session_cookie:
        browser_context.add_cookies([
            {'name': 'web_session', 'value': web_session, 'domain': ".xiaohongshu.com", 'path': "/"},
            {'name': 'a1', 'value': a1, 'domain': ".xiaohongshu.com", 'path': "/"}]
        )
        sleep(1)
    encrypt_params = context_page.evaluate("([url, data]) => window._webmsxyw(url, data)", [uri, data])
    return {
        "x-s": encrypt_params["X-s"],
        "x-t": str(encrypt_params["X-t"])
    }


xhs_client = XhsClient(cookie, sign=sign)

# get note info
note_info = xhs_client.get_note_by_id("63db8819000000001a01ead1")

# get user info
user_info = xhs_client.get_user_info("5ff0e6410000000001008400")

# get user notes
user_notes = xhs_client.get_user_notes("63273a77000000002303cc9b")

# search note
notes = xhs_client.get_note_by_keyword("小红书")
print(notes)

# get home recommend feed
recommend_type = FeedType.RECOMMEND
recommend_notes = xhs_client.get_home_feed(recommend_type)


