#!/usr/bin/python3
"""
call and use data from reddit
"""
import requests


def number_of_subscribers(subreddit):
    """Implementation of an api call."""
    if (subreddit is None) or not (isinstance(subreddit, str)):
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = (requests.get(url))
    if response.status_code == 200:
        try:
            return (response.json()['data']['subscribers'])
        except Exception:
            return 0
    else:
        return 0
