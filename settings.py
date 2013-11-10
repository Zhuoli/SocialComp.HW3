

import twitter

DEBUG = True

TESTER = 'qizhen'   # available values:  'qizhen', 'zhouli', 'xiaofeng'


COMMAND_INTERVAL = 15
SUSPICIOUS_KEYWORDS = ['health', 'realty', 'mortgage', 'fast', 'offer', 
                       'check', 'easy', 'online', 'real estate', 'finance', 
                       'money', 'airline', 'rates', 'credit', 
                       'download', 'adult', 'sex', 'music', 'game', 'following',
                       'sell', 'buy', 'diet', 'electronics', 'vehicle',
                       'contest', 'lottery', 'prize', 'loans', 'girl',
                       'free', 'porn', 'dating', 'clearance', 'singles', 'income',
                       'boss', 'earn', 'extra', 'cash', 'business', 'tax',
                       'degree', 'diploma', 'affordable', 'bargain',
                       'best', 'price', 'bucks', 'bonus', 'cheap',
                       'investment', 'lower', 'profit', 'dollars',
                       'debt', 'stock', 'chance',
                       'teen', 'wife', 'success',
                       'weight', 'bill',
                       'available', 'property', 
                       'certificate',
                       'cost', 'mate',
                       'pharmacy', 'Opportunity']
KEYWORDS_COUNT = len(SUSPICIOUS_KEYWORDS)

SPAM_CREATED_DAY_LIMIT = 7
SPAM_FRIENDS_LIMIT = 10

RECORD_LENGTH = 12

RECORD_ID = 2151667861
write_api = twitter.Api(consumer_key='otyqFeLTbZiRjlC3KhKZA',
                   consumer_secret='s4EjBZgvaTkEyRyARigkRjCzLnhlfe63WYgNgPpO4',
                   access_token_key='2151667861-soLJni1pLpJ4TcLW6BJFSOiCGex9EaCGJWXZzSg',
                   access_token_secret='XmfzG6AubTEkYucRQ0kf10bxCfwT2AM9DkVbWTsnI8oeR',
                   debugHTTP=True)

if TESTER == 'qizhen':
    crawler_api = twitter.Api(consumer_key='tBGydhPpckZw7WduxQKnkw',
                       consumer_secret='41s71xdvx2cQ0kEZqc2mAJYzGlnpaakcQUFwMnf6Gc',
                       access_token_key='2173024556-HGX8SyYrVn7L9QsyQktyPFjHARxhWEac0BGURQd',
                       access_token_secret='pxax7AcWlZ8U8f4hzMvgg5yindutEJ2Q2SRGc9EY77P7J',
                       debugHTTP=True)
    read_api = twitter.Api(consumer_key='nvZDlvDbhSuVCT6ySepw',
                       consumer_secret='3kiY4ivTmtiIiAWjkdjRy3u2ud7Db8IPHwunf3rXJw',
                       access_token_key='2187124202-mMvx2qoUEaPAWIAla701cjCBnAeuvDc1NYVSXh5',
                       access_token_secret='hA2pbcW1bZ3exZsHYnVlZe8dvbzJw4977FJ90YcGOhYSp',
                       debugHTTP=True)
    SEP = 'q'
elif TESTER == 'zhouli':
    crawler_api = twitter.Api(consumer_key='NdjOmEQsGTwgHfwLG6Q',
                       consumer_secret='XkJPnRzTBVQtZqVAaVJFsFA6egQPLWW7SSTAicBM2Q',
                       access_token_key='2173042874-dz5O0xfmQtbSDYDklXdggLQGk6yhnNaaf77nBNe',
                       access_token_secret='oHzRptFUyD8VS6zQbgx11iQAfGhqdOxZzB67Gtyllzcpp',
                       debugHTTP=True)   
    read_api = twitter.Api(consumer_key='hKrKk0cAAg87laZ1aUd0cQ',
                       consumer_secret='UeRjVWYmBi2OjHwfhwWu9PFUeTs3U6QX3jzidzFJkDw',
                       access_token_key='2187058501-ptkWSWOk5LJR0SFbJqbTxZkljRWVsTUjMZ38CXt',
                       access_token_secret='zBNASZuOMrNS9WhqdwNHtw1Eihbm2qBrVHad7QVkUUXRw',
                       debugHTTP=True)
    SEP = 'z'
elif TESTER == 'xiaofeng':
    crawler_api = twitter.Api(consumer_key='FYqPmH4FH8OYBB4ODXxR7g',
                       consumer_secret='ktcP965ujmV9pBFkcTd1MAs19OmfljIybrfK83QDA',
                       access_token_key='2173047476-f6o12AlzoWe0cAzlR8q9mkSMkUoztWc69wxXNm8',
                       access_token_secret='vfXAy7WuOFxyMBAtHMRbdXPkB3NvpCqW58LgwtIxNSz8m',
                       debugHTTP=True)   
    read_api = twitter.Api(consumer_key='hKrKk0cAAg87laZ1aUd0cQ',
                       consumer_secret='UeRjVWYmBi2OjHwfhwWu9PFUeTs3U6QX3jzidzFJkDw',
                       access_token_key='2187058501-ptkWSWOk5LJR0SFbJqbTxZkljRWVsTUjMZ38CXt',
                       access_token_secret='zBNASZuOMrNS9WhqdwNHtw1Eihbm2qBrVHad7QVkUUXRw',
                       debugHTTP=True)
    SEP = 'x'
else:  
    crawler_api = twitter.Api(consumer_key='sW6sjRTRekP8L0m4rPmVg',
                       consumer_secret='PUa0mSgDrCCW7RsCHoLMrvy2ViqgbKKEd8CIGDGw1c',
                       access_token_key='12996082-gvzUgnfZe0uIDgol1FD4y1RI1xDIyCxENO6r0BfrD',
                       access_token_secret='UJgSMVp60ip7NM9j8h9iat6iXU8nQSMoPEBA5oJaSIcba',
                       debugHTTP=True)
    read_api = twitter.Api(consumer_key='sthLEx9i79j7kJFr9kMcA',
                       consumer_secret='T1hxLPDQhtZD5fmwInI9S6idDc00NzKmouvHJYgaPs',
                       access_token_key='2176776230-zlG2U53IXpBEoij55Lx81hb1lmnHVJW2dcFCtE2',
                       access_token_secret='mliokAmXCxlio0WZkOaH5XkcLufBJ8gohxt2MP7olRfPp',
                       debugHTTP=True)
    SEP = 't'