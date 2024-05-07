#!/usr/bin/python3
'''
Queries the Reddit API and returns the number of subscribers
'''
import request


def number_of_subscribers(subreddit):
    ''' returns the number of subscribers '''
    if subreddit is None or type(subreddit) in not str:
        return 0;
    req = request.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
            headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)'}).json()
            subscribes = req.get("data", {}).get("subscribers", 0)
            return subscribes
