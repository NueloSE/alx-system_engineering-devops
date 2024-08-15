#!/usr/bin/python3
"""
call and use data from reddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
# from requests import get


# def number_of_subscribers(subreddit):
#     """Implementation of an api call."""
#     if (subreddit is None) or not (isinstance(subreddit, str)):
#         return 0
#     url = f"https://www.reddit.com/r/{subreddit}/about.json"
#     user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
#     response = get(url, headers=user_agent)
#     try:
#             return (response.json()['data']['subscribers'])
#     except Exception:
#         return 0
