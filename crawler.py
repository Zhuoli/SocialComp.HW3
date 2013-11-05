
import time
import datetime
import random
import threading  
  
import twitter_ex
import settings

def is_user_spam(user):
    current_time = time.mktime(time.gmtime())
    created_time = time.mktime(time.strptime(user.GetCreatedAt(), "%a %b %d %H:%M:%S +0000 %Y"))
    relative_created_time = datetime.timedelta(seconds = (current_time - created_time))
    return relative_created_time < datetime.timedelta(days = settings.SPAM_CREATED_DAY_LIMIT) #\
#        and user.GetFriendsCount() > settings.SPAM_FRIENDS_LIMIT
    
def is_url_spam(urls):
    suspicus_sites = ['bit.ly', 'tinyurl.com', 'is.gd', 'goo.gl', 'ow.ly', 
                      'dlvr.it', 'tiny.cc', '3.ly', 'tiny.ly']
    for url in urls:
        for site in suspicus_sites:
            if site in url.expanded_url:
                return True
    return False


                        
    

class CrawlerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_flag = False
    
    def run(self):
        keyword_index = 0
        while not self.stop_flag:
            if keyword_index < settings.KEYWORDS_COUNT- 1:
                keyword_index += 1
            else:
                keyword_index = 0
            tweets = twitter_ex.tweet_search(settings.SUSPICIOUS_KEYWORDS[keyword_index])
            
            if settings.DEBUG:
                print settings.SUSPICIOUS_KEYWORDS[keyword_index]
                print len(tweets)
            
            for tweet in tweets:
                if is_url_spam(tweet.urls):
                    user = tweet.GetUser()
                    user_id = user.GetId()
                    if not twitter_ex.is_id_in_record(user_id):
                        if is_user_spam(user):
                            print user_id
                            twitter_ex.add_to_spam_buffer(user_id)
                        else:
                            twitter_ex.add_to_normal_accounts(user_id)
        
    def stop(self):
        self.stop_flag = True
