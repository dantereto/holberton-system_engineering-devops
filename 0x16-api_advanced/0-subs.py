#!/usr/bin/python3
"""0-main"""

import requests


def number_of_subscribers(subreddit):
    """start function"""

    url_data = requests.get('https://www.reddit.com/r/{}/about.json'
                            .format(subreddit),
                            headers={'User-Agent': 'My-User'},
                            allow_redirects=False)
    if url_data.status_code != 200:
        return 0
    return url_data.json().get("data").get("subscribers")
