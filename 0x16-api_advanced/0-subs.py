import requests


def number_of_subscribers(subreddit):
    """Function to get the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'python:subscribers_count:v1.0 (by/ u/dw_mt)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.exceptions.RequestException:
        return 0
