import threading  
import logging
import time
  
import twitter_ex
import settings

class CrawlerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_flag = False
    
    def run(self):
        if settings.DEBUG:
            logger = logging.getLogger('QQ')
        while True:
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
                        if twitter_ex.is_url_spam(tweet.urls):
                            user = tweet.GetUser()
                            user_id = user.GetId()
                            if not twitter_ex.is_id_in_record(user_id):
                                if twitter_ex.is_user_spam(user):
                                    print user_id
                                    if settings.DEBUG:
                                        logger.info('newly found in search: %d' % user_id)
                                    twitter_ex.add_to_spam_buffer(user_id)
                                else:
                                    twitter_ex.add_to_normal_accounts(user_id)
                break
            except Exception as err:
                if settings.DEBUG:
                    logger.info('CrawlerThread exception')
                    logger.exception(err)
                time.sleep(300)
        
    def stop(self):
        self.stop_flag = True
