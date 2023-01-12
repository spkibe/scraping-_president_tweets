import pandas as pd
import tweepy
import json
from datetime import datetime
import s3fs

# twitter api credentials
ACCESS_TOKEN = '1539519281204969474-rdM5isKymLpROuT8sYmkeZdZ0XqpZn'
ACCESS_SECRET = 'gK0eFugb3eiCMreYKyqsakGJbTonwMDSeSd8F6ZgRnf3H'
CONSUMER_KEY = 'Bv3XuN7OPV4NvYC53Lu4UEIfj'
CONSUMER_SECRET = 'TC8HPjeb2HnHztqgjRioiOJyntOiIoJEvryuSYS2eueDvM239R'


# Setup access to API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit = True)
    return api

limit = 100
# Create API object
api = connect_to_twitter_OAuth()

print("try again")
tweets = api.user_timeline(
    screen_name = '@WilliamsRuto',
    ## return only 200 tweets
    #count = 1000,
    include_rts = True,
    # keep full text
    tweet_mode = 'extended'

).items(limit)

tweet_list = []
for tweet in tweets:
    text = tweet._json['full_text']

    refined_tweet = {
        'user': tweet.user.screen_name,
        'text' : text,
        'favorite_count': tweet.favorite_count,
        'retweet_count' : tweet.retweet_count,
        'create_at': tweet.created_at,
    }

    tweet_list.append(refined_tweet)

df = pd.DataFrame(tweet_list)

df.to_csv('william_ruto_tweets.csv')
print("done")