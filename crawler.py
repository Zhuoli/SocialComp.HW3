import threading  
import logging
  
import twitter_ex
import settings
    
def is_url_spam(urls):
    suspicus_sites = ['bit.ly', 'tinyurl.com', 'is.gd', 'goo.gl', 'ow.ly', 
                      'dlvr.it', 'tiny.cc', '3.ly', 'tiny.ly']
    for url in urls:
        for site in suspicus_sites:
            if site in url.expanded_url:
                return True
    return False
#This function is used to judge whether a url is likely to be a spamming URL.
#According to the previous studies, these sites are the most famous shortening URL providers, and URL shortening is a strong feature
#of Twitter spammers.


class CrawlerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_flag = False
    
    def run(self):
        if settings.DEBUG:
            logger = logging.getLogger('QQ')
        try:
            keyword_index = -1
            while not self.stop_flag:
                if keyword_index < settings.KEYWORDS_COUNT- 1:
                    keyword_index += 1
                else:
                    keyword_index = 0
                tweets = twitter_ex.tweet_search(settings.SUSPICIOUS_KEYWORDS[keyword_index])
                
#                 if settings.DEBUG:
#                     logger.info('%s: %d' % (settings.SUSPICIOUS_KEYWORDS[keyword_index], len(tweets)))
                
                for tweet in tweets:
                    if is_url_spam(tweet.urls):
                        user = tweet.GetUser()
                        user_id = user.GetId()
                        if not twitter_ex.is_id_in_record(user_id):
                            if twitter_ex.is_user_spam(user):
                                print user_id
                                if settings.DEBUG:
                                    logger.info('newly found spam: %d' % user_id)
                                twitter_ex.add_to_spam_buffer(user_id)
                            else:
                                twitter_ex.add_to_normal_accounts(user_id)
        except:
            if settings.DEBUG:
                logger.info('CrawlerThread exception')
        
    def stop(self):
        self.stop_flag = True
