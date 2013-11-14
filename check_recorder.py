'''
Created on Nov 5, 2013

@author: Qizhen Ruan
'''
  
import time
import re
import datetime
import settings
import twitter_ex
import twitter
      
      
def is_obsolete(status):
    current_time = time.mktime(time.gmtime())
    created_time = time.mktime(time.strptime(status.GetCreatedAt(), "%a %b %d %H:%M:%S +0000 %Y"))
    relative_created_time = datetime.timedelta(seconds = (current_time - created_time))
    return relative_created_time > datetime.timedelta(days = settings.SPAM_CREATED_DAY_LIMIT)
      
def update_tweets(first_run):
    recent_id = 0
    readed_id = 99999999999999999999L
    
    READ_EACH_TIME = 200
    user_ids = set()
    if first_run:
        status = settings.write_api.GetUserTimeline(user_id=settings.RECORD_ID, count=READ_EACH_TIME)
        read_count = len(status)
            
        while read_count > 0:

            print 'get %d of record tweets.' % read_count
            
            for item in status:
                
                if is_obsolete(item):
                    settings.write_api.DestroyStatus(item.GetId())
                    continue
                
                if item.GetId() < readed_id:
                    readed_id = item.GetId()
                    
                if item.GetId() > recent_id:
                    recent_id = item.GetId()
                    
                text = item.GetText()
                ids = re.findall(r"\D(\d{10})\D", " "+text+" ")
                for user in ids:
                    user_ids.add(user)
            status = settings.write_api.GetUserTimeline(user_id=settings.RECORD_ID, max_id=readed_id-1, count=READ_EACH_TIME)
            read_count = len(status)

    return user_ids

def is_id_suspended(user_id):
    while True:
        try:
            settings.write_api.GetUser(user_id)
            time.sleep(settings.COMMAND_INTERVAL)
            return False
        except twitter.TwitterError as err:
            if err[0][0]['code'] == 63 or err[0][0]['code'] == 34:
                
                print ('suspended id: ' + str(user_id)) 
                time.sleep(settings.COMMAND_INTERVAL)
                return True, False
            else:
                time.sleep(20* settings.COMMAND_INTERVAL)
                     
    
def main():

    posted_ids = update_tweets(True)
    print len(posted_ids)
    found = 0
    for user_id in posted_ids:
        print user_id,
        suspended = is_id_suspended(user_id)
        if suspended:  
            found += 1
            print '***** %d' % found
            
    print '========================='
    print found
    #check those recorded in cs5750 account, print those suspended IDs out

        

if __name__ == '__main__':
    main()