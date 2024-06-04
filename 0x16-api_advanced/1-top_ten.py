#!/usr/bin/python3
import requests
""" get requests"""


def top_ten(subreddit):
    """ GET the titles og the first 10 hot posts"""
    res = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Get top 10 posts"},
        params={"limit:10"},
        allow_redirects=False
    )

    if res.status_code == 200:
        for top in res.json().get("data").get("children"):
            res_data = top.get("data")
            title = res_data.get("data")
            print(title)
    else:
        print(None)
