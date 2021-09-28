#!/usr/bin/python3
"""0-main"""

count = 0
after = None

import requests


def recurse(subreddit, hot_list=[]):
    global after
    url_data = requests.get('https://www.reddit.com/r/{}/hot.json'
                            .format(subreddit),
                            params={'count': count, 'after': after},
                            headers={'User-Agent': 'My-User'},
                            allow_redirects=False)
    if url_data.status_code == 200:
        nex = url_data.json().get('data').get('after')
        if nex is not None:
            after = nex
            recurse(subreddit, hot_list)
        child = url_data.json().get('data').get('children')
        for title in child:
            hot_list.append(title.get('data').get('title'))
        return hot_list
    else:
        return None
