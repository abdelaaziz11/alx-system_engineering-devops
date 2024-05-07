#!/usr/bin/python3
'''
Queries the Reddit API and returns the number of subscribers
'''

def number_of_subscribers(subreddit):
    ''' returns the number of subscribers '''
    if not subreddit:
        return 0;
