'''
Created on Nov 5, 2013

@author: Qizhen Ruan
'''
  
import twitter_ex

                       

        
    
def main():

    posted_ids = twitter_ex.read_tweets()
    print len(posted_ids)
    found = 0
    for user_id in posted_ids:
        print user_id,
        suspended, spam = twitter_ex.is_id_suspended(user_id)
        if suspended:  
            found += 1
            print '***** %d' % found
            
    print '========================='
    print found
    #check those recorded in cs5750 account, print those suspended IDs out

        

if __name__ == '__main__':
    main()