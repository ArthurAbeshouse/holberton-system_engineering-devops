#!/usr/bin/python3
"""Requests the top 10 hottest subreddit posts"""
from requests import get


def top_ten(subreddit):
    """Returns the top 10 hottest subreddit posts"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-agent': 'agent_Flemming'}
    response = get(url, headers=headers, allow_redirects=False)
    if (response.status_code != 200):
        print('None')
    else:
        for n in range(10):
            print(response.json()['data']['children'][n]['data']['title'])
