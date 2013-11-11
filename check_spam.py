#!/usr/bin/env python
'''
Created on Nov 2, 2013

@author: Qizhen Ruan
'''



import time
import twitter


def main():
    
    api = twitter.Api(consumer_key='sW6sjRTRekP8L0m4rPmVg',
                   consumer_secret='PUa0mSgDrCCW7RsCHoLMrvy2ViqgbKKEd8CIGDGw1c',
                   access_token_key='12996082-gvzUgnfZe0uIDgol1FD4y1RI1xDIyCxENO6r0BfrD',
                   access_token_secret='UJgSMVp60ip7NM9j8h9iat6iXU8nQSMoPEBA5oJaSIcba',
                   debugHTTP=True)
    
    print_line = False 
    with open('crawled.txt', 'r') as data_file:  
        for line in data_file:
            if print_line:
                print line
                print_line = False
            else:
                if len(line) == 11:
                    try:
                        item = api.GetUser(line)
                        #When we cannot get the reply of this request, that means the account is suspended.
                        #According to the documentary of twitter API, err code 63 and 34 means the user is suspended
                    except twitter.TwitterError as err:
                        if err[0][0]['code'] == 63 or err[0][0]['code'] == 34:
                            print line
                            print_line = True
                        else:
                            print err[0][0]['message']
                    time.sleep(15)

  
#     results = api.GetFollowerIDs('ruanqizhen')
#     print results
#     for result in results:
#         item = api.GetUser(result).AsDict()
#         print item['id'], item['screen_name']



if __name__ == "__main__":
    main()
