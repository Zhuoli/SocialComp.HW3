import time
import datetime
import threading  
  
import twitter_ex
import settings

class RecorderThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_flag = False
        
    
    def run(self):
        counter = 19
        while not self.stop_flag:
            counter += 1
            if counter == 20:
                posted_ids = twitter_ex.read_tweets()
    #             if settings.DEBUG:
    #                 print posted_ids
                for user_id in posted_ids:
                    if not twitter_ex.is_id_in_record(user_id):
                        if not twitter_ex.is_id_suspended(user_id):  
                            # todo: check time
                            print user_id
                        twitter_ex.add_to_posted_spams(user_id)
                counter = 0
            time.sleep(60)
        
    def stop(self):
        self.stop_flag = True