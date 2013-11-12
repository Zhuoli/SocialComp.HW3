#!/usr/bin/env python


import twitter





def main():
    
    api = twitter.Api(consumer_key='FYqPmH4FH8OYBB4ODXxR7g',
                       consumer_secret='ktcP965ujmV9pBFkcTd1MAs19OmfljIybrfK83QDA',
                       access_token_key='2173047476-f6o12AlzoWe0cAzlR8q9mkSMkUoztWc69wxXNm8',
                       access_token_secret='vfXAy7WuOFxyMBAtHMRbdXPkB3NvpCqW58LgwtIxNSz8m',
                       debugHTTP=True)   
     
     
#     status = api.GetUserTimeline(screen_name = 'cs5750')
#     for item in status:
#         print item


    for sample in api.GetStreamSample(delimited=None, stall_warnings=None):
        print sample.GetUser()
    
#     item = api.GetUser(2174000226)
#     print item.GetId()
#     print item.GetVerified()
#     print item.GetStatusesCount()
#     print item.GetFollowersCount()
#     print item.GetFriendsCount()
#     print item.GetProfileBackgroundImageUrl()
#     print item.GetLocation()
#     print item.GetDescription()
#     print item
#     while True:
#         results = api.GetFollowerIDs('ruanqizhen')
#         print results
#         for result in results:
#             item = api.GetUser(result).AsDict()
#             print item['id'], item['screen_name']



if __name__ == "__main__":
    main()
