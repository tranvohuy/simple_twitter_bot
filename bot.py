import tweepy
import datetime

from local_settings import *  

auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
auth.set_access_token(Access_token, Access_token_secret)
api = tweepy.API(auth)

if __name__ == '__main__':
    print("about to update status...")
    api.update_status('Right now it is ' + str(datetime.datetime.now()))
