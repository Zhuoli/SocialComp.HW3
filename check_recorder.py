'''
Created on Nov 5, 2013

@author: Qizhen Ruan
'''
import time
import datetime
 
  
import twitter_ex
import settings
                       

        
    
def main():

    posted_ids = twitter_ex.read_tweets()
    found = 0
    for user_id in posted_ids:
        if twitter_ex.is_id_suspended(user_id):  
            found += 1
    
    print len(posted_ids)
    print found

        

if __name__ == '__main__':
    main()