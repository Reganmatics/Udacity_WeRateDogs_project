#!/usr/bin/python3

_author_ = "Regan"

import json
import pandas as pd


df_list = []

with open("tweet-json.txt", encoding='utf-8') as json_file:
    for tweet_id in json_file:
        tweet = json.loads(tweet_id)

        tweet_id        = tweet['id']
        retweet_count   = tweet['retweet_count']
        fav_count       = tweet['favorite_count']

        df_list.append({'tweet_id':tweet_id,
            'retweet_count':retweet_count, 'favorite_count':fav_count})

df_3 = pd.DataFrame(df_list, columns = ['tweet_id', 'retweet_count','favorite_count'])
print(df_3)
