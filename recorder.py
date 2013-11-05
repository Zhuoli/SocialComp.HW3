import time
import datetime
import threading  
  
import twitter_ex
import settings

def is_user_spam(user):
    current_time = time.mktime(time.gmtime())
    created_time = time.mktime(time.strptime(user.GetCreatedAt(), "%a %b %d %H:%M:%S +0000 %Y"))
    relative_created_time = datetime.timedelta(seconds = (current_time - created_time))
    return relative_created_time < datetime.timedelta(days = settings.SPAM_CREATED_DAY_LIMIT) \
        and user.GetFriendsCount() > settings.SPAM_FRIENDS_LIMIT
    
                       
    

class RecorderThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_flag = False
        
    
    def run(self):
        while not self.stop_flag:
            posted_ids = twitter_ex.read_tweets()
#             if settings.DEBUG:
#                 print posted_ids
            for user_id in posted_ids:
                if not twitter_ex.is_id_in_record(user_id):
                    if not twitter_ex.is_id_suspended(user_id):  
                        # todo: check time
                        print user_id
                    twitter_ex.add_to_posted_spams(user_id)

                        
            time.sleep(600)
        
    def stop(self):
        self.stop_flag = True