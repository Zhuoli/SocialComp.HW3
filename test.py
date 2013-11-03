#!/usr/bin/env python


import twitter
import inspect




def main():
    
    api = twitter.Api(consumer_key='sW6sjRTRekP8L0m4rPmVg',
                   consumer_secret='PUa0mSgDrCCW7RsCHoLMrvy2ViqgbKKEd8CIGDGw1c',
                   access_token_key='12996082-gvzUgnfZe0uIDgol1FD4y1RI1xDIyCxENO6r0BfrD',
                   access_token_secret='UJgSMVp60ip7NM9j8h9iat6iXU8nQSMoPEBA5oJaSIcba',
                   debugHTTP=True)
     
#     item = api.GetUser('21650541112') #screen_name = 'BatuTurguteli17')
#     print item.GetVerified()
#     print item.GetStatusesCount()
#     print item.GetFollowersCount()
#     print item.GetFriendsCount()
#     print item.GetProfileBackgroundImageUrl()
#     print item.GetLocation()
#     print item.GetDescription()
#     print item
    while True:
        results = api.GetFollowerIDs('ruanqizhen')
        print results
#         for result in results:
#             item = api.GetUser(result).AsDict()
#             print item['id'], item['screen_name']



if __name__ == "__main__":
    main()
