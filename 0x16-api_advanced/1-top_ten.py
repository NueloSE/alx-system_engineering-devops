#!/usr/bin/python3
"""implement reading from reddit api"""

import requests

def top_ten(subreddit):
	"""gets top ten items in subreddit api"""
	if subreddit is None or not isinstance(subreddit, str):
		print("None")
	try:
		url = f"http://www.reddit.com/r/{subreddit}/hot.json?limit=10"
		response = requests.get(url)
		result = response.json()["data"]["children"]
		for item in result:
			print(item["data"]['title'])
	except Exception:
		print("None")
