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
        if twitter_ex.is_id_suspended(user_id):  
            found += 1
            print '***** %d' % found
            
    print '========================='
    print found

        

if __name__ == '__main__':
    main()