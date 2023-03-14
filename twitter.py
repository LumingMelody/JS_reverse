# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 16:45
# @Author  : 蔍鸣霸霸
# @FileName: twitter.py
# @Software: PyCharm
# @Blog    ：只因你太美

import re
import json
import requests
from urllib.parse import urlencode
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from loguru import logger

proxies = {'https': 'http://127.0.0.1:4780'}


def get_infos():
    url = "https://abs.twimg.com/responsive-web/client-web/main.8644ab25.js"
    response = requests.get(url, proxies=proxies, verify=False)
    authorization = "Bearer " + re.search("(AAAAA.*?)\"", response.text).group(1)
    user_tweets = re.search('queryId:\"(.{22})\",operationName:\"UserTweets\",', response.text).group(1)
    user_by_screen_name = re.search('queryId:\"(.{22})\",operationName:\"UserByScreenName\",', response.text).group(1)
    gt_headers = {
        'authority': 'api.twitter.com',
        'content-length': '0',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'x-twitter-client-language': 'zh-cn',
        'sec-ch-ua-mobile': '?0',
        'authorization': authorization,
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/97.0.4692.99 Safari/537.36',
        'x-twitter-active-user': 'yes',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'origin': 'https://twitter.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://twitter.com/',
        'accept-language': 'zh-CN,zh;q=0.9',
    }
    logger.debug('开始获取guest_token...')
    response_gt = requests.post('https://api.twitter.com/1.1/guest/activate.json', proxies=proxies, headers=gt_headers,
                                verify=False)
    return dict(
        guest_token=response_gt.json()['guest_token'],
        authorization=authorization,
        user_tweets=user_tweets,
        user_by_screen_name=user_by_screen_name
    )


infos = get_infos()


class TwitterBase():
    def __init__(self):
        self.infos = infos

    def get_headers(self, **kwargs):
        return {
            'x-guest-token': self.infos['guest_token'],
            'authorization': self.infos['authorization'],
            'authority': 'twitter.com',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'x-twitter-client-language': 'zh-cn',
            'sec-ch-ua-mobile': '?0',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/97.0.4692.99 Safari/537.36',
            'x-twitter-active-user': 'yes',
            'sec-ch-ua-platform': '"Windows"',
            'accept': '*/*',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://twitter.com/'.format(kwargs['username']),
            'accept-language': 'zh-CN,zh;q=0.9',
        }


class TwitterUserByScreenName(TwitterBase):
    Uri = 'https://twitter.com/i/api/graphql/{}/UserByScreenName?'

    def get_url(self, **kwargs):
        params_data = {
            "variables": json.dumps({
                "screen_name": kwargs['username'],
                "withSafetyModeUserFields": "true",
                "withSuperFollowsUserFields": "true"
            })
        }
        return self.Uri.format(self.infos['user_by_screen_name']) + urlencode(params_data)


class TwitterGuess(TwitterBase):
    Uri = 'https://twitter.com/i/api/graphql/{}/UserTweets?'

    def get_url(self, **kwargs):
        variables = {
            "userId": kwargs['userId'],
            "count": kwargs['count'] if 'conut' in kwargs else 40,
            "includePromotedContent": "true",
            "withQuickPromoteEligibilityTweetFields": "true",
            "withSuperFollowsUserFields": "true",
            "withBirdwatchPivots": "false",
            "withDownvotePerspective": "false",
            "withReactionsMetadata": "false",
            "withReactionsPerspective": "false",
            "withSuperFollowsTweetFields": "true",
            "withVoice": "true",
            "withV2Timeline": "false",
            "__fs_interactive_text": "false",
            "__fs_dont_mention_me_view_api_enabled": "false"
        }
        if 'cursor' in kwargs:
            variables.update({'cursor': kwargs['cursor']})
        params_data = {"variables": json.dumps(variables)}
        url = self.Uri.format(self.infos['user_tweets']) + urlencode(params_data)
        return url


def requestUID(username):
    twn = TwitterUserByScreenName()
    get_user_url = twn.get_url(username=username)
    headers = twn.get_headers(username=username)
    user_response = requests.get(url=get_user_url, headers=headers, verify=False, proxies=proxies)
    user_rest_id = user_response.json()['data']['user']['result']['rest_id']
    return user_rest_id


def requestTW(user_rest_id, username, cursor=None):
    get_guess_url = twg.get_url(userId=user_rest_id, cursor=cursor)
    get_guess_headers = twg.get_headers(username=username)
    guess_response = requests.get(url=get_guess_url, headers=get_guess_headers, verify=False, proxies=proxies).json()
    cursor = parse_response(guess_response)
    return cursor


def parse_response(twitter_content):
    instructionList = twitter_content['data']['user']['result']['timeline']['timeline']['instructions']
    cursor = None
    instructions = None

    for ins in instructionList:
        if ins['type'] == 'TimelineAddEntries':
            instructions = ins['entries']
            break

    for user_twitter in instructions:
        if 'cursor-bottom' in user_twitter['entryId']:
            cursor = user_twitter['content']['value']
        if not user_twitter['content'].get('itemContent'):
            continue
        if not user_twitter['content']['itemContent'].get('tweet_results'):
            logger.debug("所有推文获取完毕")
            break
        legacy = user_twitter['content']['itemContent']['tweet_results']['result'].get('legacy')
        if not legacy: continue
        full_text = legacy['full_text']
        lang = legacy['lang']
        quote_count = legacy['quote_count']  # 引用
        favorite_count = legacy['favorite_count']  # 喜欢
        reply_count = legacy['reply_count']  # 回复
        retweet_count = legacy['retweet_count']  # 转推
        id_str = legacy['id_str']
        created_at = legacy['created_at']
        print(id_str, full_text[:50])

    logger.debug(f"下一页cursor:{cursor}")
    return cursor


if __name__ == '__main__':
    username = 'frankiemad1'
    user_rest_id = "2988004682"  # requestUID(username)
    twg = TwitterGuess()
    logger.debug(f"USERID:{user_rest_id}")

    cursor = requestTW(user_rest_id, username)
    while 1:
        if cursor:
            cursor = requestTW(user_rest_id, username, cursor)
        else:
            break
