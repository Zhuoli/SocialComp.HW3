'''
Created on Nov 3, 2013

@author: Qizhen Ruan
'''

import time
import inspect
import re
import twitter
import settings
import logging


if settings.DEBUG:
    logger = logging.getLogger('QQ')
    logger.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # create file handler which logs even debug messages
    fh = logging.FileHandler('5750tweetspam.log')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    fh.setFormatter(formatter)
    #ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)


normal_accounts = set()
posted_spams = set()
spam_buffer = set()

record_recent_id = 396755128352784384
keword_recent_id = {}


def handle_rate_exceeded(err):
    if settings.DEBUG:
        logger.error(inspect.stack()[1][3] + err[0][0]['message'])
    if err[0][0]['code'] == 88:
        time.sleep(10 * settings.COMMAND_INTERVAL)
    else:
        raise Exception(err)
    
def tweet_search(keyword):
    while True:
        try:
            last_id = keword_recent_id.get(keyword, 0)
            tweets = settings.crawler_api.GetSearch(keyword, since_id=last_id, count = 5000, result_type="recent")
            if len(tweets) > 0:
                last_id = tweets[0].GetId()
            keword_recent_id[keyword] = last_id
            time.sleep(settings.COMMAND_INTERVAL)
            return tweets
        except twitter.TwitterError as err:
            handle_rate_exceeded(err)
            
def post_result(items):
    if settings.DEBUG:
        logger.info('post to twitter') 
        logger.info(items) 
    while True:
        try:
            id_str = [str(i) for i in items]
            for item in items:
                add_to_posted_spams(item)
            items.clear()
            settings.record_api.PostUpdates(' '.join(id_str)) 
            time.sleep(settings.COMMAND_INTERVAL) 
            break    
        except twitter.TwitterError as err:
            handle_rate_exceeded(err)

def read_tweets():
    global record_recent_id
    while True:
        try:
            status = settings.record_api.GetUserTimeline(user_id=settings.RECORD_ID, since_id=record_recent_id)
            user_ids = set()
            for item in status:
                if item.GetId() > record_recent_id:
                    record_recent_id = item.GetId()
                text = item.GetText()
                ids = re.findall(r"\D(\d{10})\D", " "+text+" ")
                for user in ids:
                    user_ids.add(user)
            time.sleep(settings.COMMAND_INTERVAL)
            return user_ids
        except:
            return set()
  
def is_id_suspended(user_id):
    while True:
        try:
            settings.record_api.GetUser(user_id)
            time.sleep(settings.COMMAND_INTERVAL)
            return False
        except twitter.TwitterError as err:
            if err[0][0]['code'] == 63 or err[0][0]['code'] == 34:
                
                if settings.DEBUG:
                    logger.info('suspended id: ' + str(user_id)) 
                time.sleep(settings.COMMAND_INTERVAL)
                return True
            else:
                handle_rate_exceeded(err)
        
                        
def is_id_in_record(user_id):
    return user_id in normal_accounts or user_id in posted_spams or user_id in spam_buffer

def add_to_normal_accounts(user_id):
    if len(normal_accounts) > 100000:
        normal_accounts.clear()
    normal_accounts.add(user_id)
#     if settings.DEBUG:
#         logger.info('total accounts: %d' % len(normal_accounts)) 
        
def add_to_posted_spams(user_id):
    posted_spams.add(user_id)
    
def add_to_spam_buffer(user_id):
    spam_buffer.add(user_id)
    if len(spam_buffer) >= settings.RECORD_LENGTH:
        post_result(spam_buffer)
        
    
    