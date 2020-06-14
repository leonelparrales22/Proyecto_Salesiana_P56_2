import tweepy
import csv
import pandas as pd


def buscar_tweets(texto):
    consumer_key = "cojy2FNj32qiygPcNbh8gwNBq"
    consumer_secret = "EDHc16EJdOt3Z6sDWoYpEwpDNG0I6zSOVr5Amd9xvmytmSbyOi"
    access_token = "252235347-YxCynAKgrMayf8A1XmfyPgdMA5y05lcB3rzc0qFP"
    access_token_secret = "JxJAh3aXPzQlz40R55NLO2MRpizUHS8b4ci2DYiBNt9Fi"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit="TRUE", wait_on_rate_limit_notify="TRUE")
    csvFile = open('tweets.csv', 'a')

    csvWriter = csv.writer(csvFile)
    ##Buscar Tweets
    cont = 0
    tweets = []
    for tweet in tweepy.Cursor(api.search, q=texto, lang="es", tweet_mode="extended",
                               geocode=" -1.39459,-78.39924,250km").items(30):
        if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
            var = tweet._json["full_text"]
            tweets.append(var)

    for i in enumerate(tweets):
        print(i)

    # Paso de tweets a archivo csv

    df = df = pd.DataFrame(tweets)
    df.to_csv('model/tweets.csv')