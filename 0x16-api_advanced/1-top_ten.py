#!/usr/bin/python3
"""0-main"""

import requests


def top_ten(subreddit):

    url_data = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                            .format(subreddit),
                            headers={'User-Agent': 'My-User'},
                            allow_redirects=False)
    if url_data.status_code == 200:
        child = url_data.json().get('data').get('children')
        for title in child:
            print(title.get('data').get('title'))
    else:
        print(None)
