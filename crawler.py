#!/usr/bin/env python
'''
connect to Twitter and output user IDs that will be banned
Created on Oct 31, 2013  @Qizhen
'''

import time
import datetime
import random
    
import twitter_ex
import settings



       
def is_user_spam(user):
    current_time = time.mktime(time.gmtime())
    created_time = time.mktime(time.strptime(user.GetCreatedAt(), "%a %b %d %H:%M:%S +0000 %Y"))
    relative_created_time = datetime.timedelta(seconds = (current_time - created_time))
    return relative_created_time < datetime.timedelta(days = settings.SPAM_CREATED_DAY_LIMIT) \
        and user.GetFriendsCount() > settings.SPAM_FRIENDS_LIMIT
    
def is_url_spam(urls):
    suspicus_sites = ['bit.ly', 'tinyurl.com', 'is.gd', 'goo.gl', 'ow.ly', 
                      'dlvr.it', 'tiny.cc', '3.ly', 'tiny.ly']
    for url in urls:
        for site in suspicus_sites:
            if site in url.expanded_url:
                return True
    return False
            
def crawl():

    spammers = set()
    normal_user = set()
    
    while True:
        keyword_index = random.randrange(0, settings.KEYWORDS_COUNT)
        tweets = twitter_ex.tweet_search(settings.crawler_api, settings.SUSPICIOUS_KEYWORDS[keyword_index])
        for tweet in tweets:
            if is_url_spam(tweet.urls):
                user = tweet.GetUser()
                user_id = user.GetId()
                if not user_id in normal_user and not user_id in spammers:
                    if is_user_spam(user):
                        print user_id
                        print user
                        spammers.add(user_id)
                    else:
                        normal_user.add(user_id)
                        
    



