#!/usr/bin/env python
#This is our trial version, to test most of API used...
'''connect to Twitter and output user IDs that will be banned'''

import time
import datetime
import logging
import random
import twitter
from dateutil.parser import parser

COMMAND_INTERVAL = 15
SUSPICIOUS_KEYWORDS = ['money', 'finance', 'mortgage', 'health', 'airline',
                       'download', 'adult', 'sex', 'music', 'game', 'following',
                       'sell', 'buy', 'diet', 'jewelery', 'electronics', 'vehicle',
                       'contest', 'lottery', 'prize', 'loans', 'realty', 'girl',
                       'free', 'porn', 'dating']
KEYWORDS_COUNT = len(SUSPICIOUS_KEYWORDS)

# initialize this twitter API
# @Author: Zhuoli
def initialize():
    #user infor for cs5750
    api = twitter.Api(consumer_key='otyqFeLTbZiRjlC3KhKZA',
                   consumer_secret='s4EjBZgvaTkEyRyARigkRjCzLnhlfe63WYgNgPpO4',
                   access_token_key='2151667861-soLJni1pLpJ4TcLW6BJFSOiCGex9EaCGJWXZzSg',
                   access_token_secret='XmfzG6AubTEkYucRQ0kf10bxCfwT2AM9DkVbWTsnI8oeR',
                   debugHTTP=True)
    logging.basicConfig(filename='5750tweetspam.log',level=logging.ERROR)
    return api

def handle_twitter_error(err):
    logging.exception(err)
    #logging.error('%s error: %s' % (inspect.stack()[1][3], err.message()[0]))
    time.sleep(COMMAND_INTERVAL)


    
def get_users_search(api, keyword):
    while True:
        try:
            seeds = api.GetUsersSearch(keyword, count=30)
            time.sleep(COMMAND_INTERVAL)
            return seeds
        except twitter.TwitterError as errs:
            handle_twitter_error(errs)

def get_followers(api, id):
    try:
        followers = api.GetFollowerIDs(id, count=5000, total_count=5000)
        time.sleep(COMMAND_INTERVAL)
        return followers
    except twitter.TwitterError as errs:
        handle_twitter_error(errs)
        return []
        
def get_user(api, id):
    try:
        user = api.GetUser(id)
        time.sleep(COMMAND_INTERVAL)
        return user
    except twitter.TwitterError as errs:
        handle_twitter_error(errs)    
        
def is_user_spam(user):
    is_spam = True
    current_time = time.mktime(time.gmtime())
    created_time = time.mktime(time.strptime(user.GetCreatedAt(), "%a %b %d %H:%M:%S +0000 %Y"))
    relative_created_time = datetime.timedelta(seconds = (current_time - created_time))
    is_spam &= relative_created_time < datetime.timedelta(days=7)
#     is_spam &= user.GetStatusesCount() > 5
#     is_spam &= user.GetFriendsCount() > 10
#     is_spam &= not user.GetLocation()

    #print user.GetProfileBackgroundImageUrl()
    return is_spam

#@Author: Zhuoli
def setPost(api,idlist,id):
  if len(idlist) >= 10:
    text = ''
    while(len(idlist) > 0):
      item = idlist.pop()
      text = text + ' ' + str(item)
    idlist.append(id)
    api.PostUpdates(text)
  else:
    idlist.append(id)
#@Author: Zhuoli
def getTweets(api,user_id):
  spam_id_list = []
  statuses = api.GetUserTimeline(user_id)
  for statue in statuses:
    if isListOfID(statue.text):
      sublist = text2list(statue.text)
      spam_id_list.extend(sublist)
  return spam_id_list
#@Author: Zhuoli
#GIVEN: A [lain text text
#RETURN: TRUE if it is a list of id
def isListOfID(text):
  items = text.split(' ')
  for item in items:
    try:
      if len(item) != 10:
        return False
      int(item)
    except ValueError as errs:
      return False
  return True
#@Author: Zhuoli
#GIVEN: a plain text tweet
#RETURN: A list of account id number
def text2list(text):
  texts = []
  for item in text.split(' '):
    try:
      texts.append(int(item))
    except ValueError as errs:
      pass
  return texts

#@Author: Zhuoli
def filterSpamAccount(api,spam_id_list):
  spams = []
  while len(spam_id_list) > 0:
    spam = spam_id_list.pop()
    if isSuspicious(api,spam):
      spams.append(spam)
  spam_id_list.extend(spams)

#@Author: Zhuoli
def isSuspicious(api,spam_id):
  SUSPICIOUS_DAY = 7
  p = parser()
  user = api.GetUser(user_id = spam_id)
  status = user.Status
  creation = p.parse(status.created_at)
  current = time.localtime()
  dif = (current[0] - creation.year) * 365 +(current[1] - creation.month) * 30 +(current[2] - creation.day)
  if dif > SUSPICIOUS_DAY:
    return False
  else:
    try:
      item = api.GetUser(user_id = spam_id)
      return true
    except twitter.TwitterError as err:
      return False
    return True


def main():
    CS5750_ID = 2151667861
    api = initialize()
    spammers = set()
    normal_user = set()
    idlist = []
    while True:
        keyword_index = random.randrange(0, KEYWORDS_COUNT)
        seeds = get_users_search(api, SUSPICIOUS_KEYWORDS[keyword_index])
        for seed in seeds:
            followers = get_followers(api, seed.id)
            for follower in followers:
                user = get_user(api, follower)
                user_id = user.GetId()
                if not user_id in normal_user and not user_id in spammers:
                    if user != None and is_user_spam(user):
                        setPost(api,idlist,user_id)
                        print user_id
                        spammers.add(user_id)
                    else:
                        normal_user.add(user_id)
   



if __name__ == "__main__":
    main()

''' Instruction:
  *Methods:
  ---api.GetUser(user)
  ---api.GetFriends()
  ---api.GetFollowers()
  ---api.GetRepllies()
  ---api.GetRetweeters()
  ---api.GetRetweets()
  ---api.GetUserRetweets()   
  ---api.GetUserTimeLine()
  ---api.GetUserSearch()
  ---api.GetSearch()        // Return Status object
  ---api.GetTrendsCurrent() // Get the current top trending topics
  ---api.GetTrendsWoeid()   // Return the top 1- trending topics for 
                            // a specific WOEID
  ---api.UsersLookup()      // Fetch extended information for this user
                            // returns a list of twitter.User objects for 
                            // the requested users

  *Class:
  User: id,name,screen_name,location
  Status: contributors, coordinates, created_at, created_at_in_seconds,
          favorited,favorite_count,id,lang,place,source,text,truncated,
          location
  
'''

