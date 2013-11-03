'''
connect to Twitter and output user IDs that will be banned
Created on Oct 29, 2013  @author: Qizhen
'''

import twitter

TESTER = ''
COMMAND_INTERVAL = 15
SUSPICIOUS_KEYWORDS = ['money', 'finance', 'mortgage', 'health', 'airline',
                       'download', 'adult', 'sex', 'music', 'game', 'following',
                       'sell', 'buy', 'diet', 'jewelery', 'electronics', 'vehicle',
                       'contest', 'lottery', 'prize', 'loans', 'realty', 'girl',
                       'free', 'porn', 'dating', 'clearance', 'singles', 'income',
                       'boss', 'earn', 'extra', 'cash', 'business', 'tax',
                       'degree', 'diploma', 'offer', 'affordable', 'bargain',
                       'best', 'beneficiary', 'price', 'bucks', 'bonus', 'cheap',
                       'check', 'rates', 'credit', 'easy', 'Potential earnings',
                       'fast', 'investment', 'lower', 'profit', 'dollars',
                       'debt', 'stock', 'chance', 'passwords', 'solution',
                       'teen', 'wife', 'success', 'cures', 'viagra', 'xanax',
                       'weight', 'bill', 'inventory', 'Additional income',
                       'available', 'fingertips', 'online' 'property' 'real estate',
                       'All natural', 'Apply Online', 'Refinance home', 'Full refund',
                       'Removes wrinkles', 'certificate', 'Reverses aging', 
                       'Limited time only', 'Lose weight', 'MLM', 'cost', 'mate',
                       'pharmacy', 'Opportunity', 'Pennies']
KEYWORDS_COUNT = len(SUSPICIOUS_KEYWORDS)

SPAM_CREATED_DAY_LIMIT = 3
SPAM_FRIENDS_LIMIT = 10

record_api = twitter.Api(consumer_key='otyqFeLTbZiRjlC3KhKZA',
                   consumer_secret='s4EjBZgvaTkEyRyARigkRjCzLnhlfe63WYgNgPpO4',
                   access_token_key='2151667861-MfgX0cunxe9S6lgTYo1mFBpxIWtcDG1zmNLbJcR',
                   access_token_secret='oeYIUHT6px0U5Euu9bZ9iNhorJuwcgGwDF5lwlCER4317',
                   debugHTTP=True)



if TESTER == 'qizhen':
    crawler_api = twitter.Api(consumer_key='sW6sjRTRekP8L0m4rPmVg',
                       consumer_secret='PUa0mSgDrCCW7RsCHoLMrvy2ViqgbKKEd8CIGDGw1c',
                       access_token_key='12996082-gvzUgnfZe0uIDgol1FD4y1RI1xDIyCxENO6r0BfrD',
                       access_token_secret='UJgSMVp60ip7NM9j8h9iat6iXU8nQSMoPEBA5oJaSIcba',
                       debugHTTP=True)
elif TESTER == 'zhouli':
    crawler_api = twitter.Api(consumer_key='sW6sjRTRekP8L0m4rPmVg',
                       consumer_secret='PUa0mSgDrCCW7RsCHoLMrvy2ViqgbKKEd8CIGDGw1c',
                       access_token_key='12996082-gvzUgnfZe0uIDgol1FD4y1RI1xDIyCxENO6r0BfrD',
                       access_token_secret='UJgSMVp60ip7NM9j8h9iat6iXU8nQSMoPEBA5oJaSIcba',
                       debugHTTP=True)   
elif TESTER == 'xiaofeng':
    crawler_api = twitter.Api(consumer_key='sW6sjRTRekP8L0m4rPmVg',
                       consumer_secret='PUa0mSgDrCCW7RsCHoLMrvy2ViqgbKKEd8CIGDGw1c',
                       access_token_key='12996082-gvzUgnfZe0uIDgol1FD4y1RI1xDIyCxENO6r0BfrD',
                       access_token_secret='UJgSMVp60ip7NM9j8h9iat6iXU8nQSMoPEBA5oJaSIcba',
                       debugHTTP=True)   
else:  
    crawler_api = twitter.Api(consumer_key='sW6sjRTRekP8L0m4rPmVg',
                       consumer_secret='PUa0mSgDrCCW7RsCHoLMrvy2ViqgbKKEd8CIGDGw1c',
                       access_token_key='12996082-gvzUgnfZe0uIDgol1FD4y1RI1xDIyCxENO6r0BfrD',
                       access_token_secret='UJgSMVp60ip7NM9j8h9iat6iXU8nQSMoPEBA5oJaSIcba',
                       debugHTTP=True)