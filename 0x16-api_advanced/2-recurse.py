#!/usr/bin/python3
"""Returns a list containing the titles
   of all the hottest articles for a given subreddit"""
from requests import get


def recurse(subreddit, hot_list=[], after=""):
    """Returns a list containing the titles
       of all the hottest articles for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit, after)
    headers = {"User-agent": "agent_Flemming"}
    params = {"after": after}
    if (after is ""):
        response = get(url, headers=headers, allow_redirects=False)
    else:
        response = get(
            url,
            headers=headers,
            allow_redirects=False,
            params=params)
    if (response.status_code != 200):
        return None
    else:
        jsonresponse = response.json()
        data = jsonresponse["data"]["after"]
        parent = jsonresponse["data"]["children"]
        for post in parent:
            hot_list.append(post["data"]["title"])
        if data is None:
            return hot_list
        return recurse(subreddit, hot_list, data)
