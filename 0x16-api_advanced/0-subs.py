#!/usr/bin/python3
"""Requests amount of subreddit subscribers"""
from requests import get


def number_of_subscribers(subreddit):
    """Returns the amount of subreddit subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-agent': 'agent_Flemming'}
    response = get(url, headers=headers, allow_redirects=False)
    if (response.status_code != 200):
        return 0
    return response.json()['data']['subscribers']
