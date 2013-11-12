import threading  
import logging
  
import twitter_ex
import settings
    
class StreamerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_flag = False
    
    def run(self):
        if settings.DEBUG:
            logger = logging.getLogger('QQ')
        try:
            for tweet in settings.stream_api.GetStreamSample():
                if self.stop_flag:
                    break
                if tweet.GetId():
                    if twitter_ex.is_url_spam(tweet.urls):
                        user = tweet.GetUser()
                        user_id = user.GetId()
                        if not twitter_ex.is_id_in_record(user_id):
                            if twitter_ex.is_user_spam(user):
                                print user_id
                                if settings.DEBUG:
                                    logger.info('newly found in stream: %d' % user_id)
                                twitter_ex.add_to_spam_buffer(user_id)
                            else:
                                twitter_ex.add_to_normal_accounts(user_id)
        except Exception as err:
            if settings.DEBUG:
                logger.info('StreamerThread exception')
        
    def stop(self):
        self.stop_flag = True
