import sys
import tweepy
import keys
import datetime, time

auth = tweepy.OAuthHandler(keys.TWITTER_APP_KEY, keys.TWITTER_APP_SECRET)
auth.set_access_token(keys.TWITTER_KEY, keys.TWITTER_SECRET)
api = tweepy.API(auth)

def get_tweets(api,username):
    page = 1
    deadend = False
    while True:
        tweets = api.user_timeline(username, page = page)

        for tweet in tweets:
            if (datetime.datetime.now() - tweet.created_at).days < 1:
                print(tweet.text.encode("utf-8"))
            else:
                deadend = True
                return
        if not deadend:
            page+1
            time.sleep(500)

get_tweets(api, "GDOT_I75_ATL")