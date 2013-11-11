Twitter Spam Killer:
The purpose of this project is to find these potential spam twitter accounts
Homework 3 of Qizhen Ruan, Zhuoli Liang, Xiaofeng Yang

-------------------------------------

To obtain suspicious accounts, run 5750tweetspam.py with our created accounts.
Debug is set False in testing(clean output), True in debugging(Debugging helpful outputs).

-------------------------------------

We registered several twitter accounts, running our 5750tweetspam.py simultaneously to record the spammer user id as tweets at our main account.
The spammer information is stored in the main account, and is ready to read when we need to analyze the feature of spammers.

Directory 'oauthlib', 'requests','requests_oauthlib' are three existing twitter API libary, from which we can use documented functions to get tweets
and user information.

For example:
     followers count : Object, User.followers_count
     friends count     : Object, User.friends_count
     verified               : Object, User.verified
     time of creation : Object, User.created_at
     listed count        : Object, User.listed_count
     tweet content    : Object, Status.text
     special topic      : Method, api.GetSearch(term=’ ’)   return a list of Status objects


------------------------------------
The main steps are

1. Record suspicious accounts:
Search hot keywords like “money”, “free”, “download”.
Use the results accounts as seeds
Get all followers of the seed accounts
Check if the followers are suspected spammers
When 8 of the new accounts are found, post a new tweet on cs5750 account

2.
Read tweets on cs5750
Get all accounts posted on it
Check if an account has already been suspended.
Make Sure it is from 1 day to 3 days, this time period is determined by our trial and error: most accounts suspended are generated within this
time span, and it is justifiable to check only these new accounts.
If not, then return

3.Exception
We try to cover various kinds of exceptions, to have the program running robustly in days.
If the API function cannot visit cs5750, or all accounts listed on cs5750 has been returned, then crawl the accounts itself
-------------------------------------

5750tweetspam records suspended users and our judged spammers.




