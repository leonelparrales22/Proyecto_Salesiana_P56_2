import tweepy
import csv
import pandas as pd

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
for tweet in tweepy.Cursor(api.search, q="coronavirus", lang="es", tweet_mode="extended",
                           geocode=" -1.39459,-78.39924,250km",
                           until="2020-05-28").items(2000):
    if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
        # print(tweet._json["full_text"])
        # var = tweet.created_at , tweet._json["full_text"]
        var = tweet._json["full_text"]
        # var2 =
        # cont = cont + 1
        # tweets.append(var2)
        tweets.append(var)

# convert 'tweets' list to pandas.DataFrame
# tweets_df = pd.DataFrame(vars(tweets[i]) for i in range(len(tweets)))

# define file path (string) to save csv file to
# FILE_PATH = "tweets.csv"

# use pandas to save dataframe to csv
# tweets_df.to_csv(FILE_PATH)
# print("El número de tweets es: ", cont)

for i in enumerate(tweets):
    print(i)

# Paso de tweets a archivo csv

df = df = pd.DataFrame(tweets)
df.to_csv('tweets.csv')
