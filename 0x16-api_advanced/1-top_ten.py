#!/usr/bin/python3
"""first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """ function prints titles of the first 10
    posts or None if subreddit is invalid
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Get 10 hottest post'}
    params = {'limit': '10'}

    response = requests.get(
        url,
        headers=headers,
        params=params)

    if response.status_code == 200:
        for posts in response.json().get('data').get('children'):
            post = posts.get('data')
            title = post.get('title')
            print(title)
    else:
        print(None)
