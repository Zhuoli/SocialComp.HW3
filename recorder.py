import time
import logging
import threading  
  
import twitter_ex
import settings

class RecorderThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_flag = False
        
    
    def run(self):
        try:
            counter = 29
            while not self.stop_flag:
                counter += 1
                if counter == 30:
                    posted_ids = twitter_ex.read_tweets()
        #             if settings.DEBUG:
        #                 print posted_ids
                    for user_id in posted_ids:
                        if not twitter_ex.is_id_in_record(user_id):
                            suspend, spam = twitter_ex.is_id_suspended(user_id)
                            if not suspend and spam:  
                                print user_id
                            twitter_ex.add_to_posted_spams(user_id)
                    counter = 0
                time.sleep(60)
        except:
            if settings.DEBUG:
                logger = logging.getLogger('QQ')
                logger.info('RecorderThread exception')
        
    def stop(self):
        self.stop_flag = True