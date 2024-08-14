#!/usr/bin/python3
"""
call and use data from reddit
"""
from requests import get


def number_of_subscribers(subreddit):
    """Implementation of an api call."""
    if (subreddit is None) or not (isinstance(subreddit, str)):
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    response = get(url, headers=user_agent)
    try:
            return (response.json()['data']['subscribers'])
    except Exception:
        return 0
