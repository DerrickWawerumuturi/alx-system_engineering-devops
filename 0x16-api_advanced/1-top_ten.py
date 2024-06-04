# Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

# Requirements:

# Prototype: def top_ten(subreddit)
# If not a valid subreddit, print None.
# NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

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
