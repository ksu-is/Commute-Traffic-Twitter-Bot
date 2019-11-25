import tweepy
import keys
import datetime, time

def get_tweets(api,username):
    page = 1
    deadend = False
    while True:
        tweets = api.user_timeline(username, page = page)

        for tweet in tweets:
            if (datetime.datetime.now() - tweet.created_at).days < 2:
                print(tweet.text.encode("utf-8"))
            else:
                deadend = True
                return
        if not deadend:
            page+1
            time.sleep(500)

get_tweets(api, "SpaceX")