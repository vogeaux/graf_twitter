import snscrape.modules.twitter as sntwitter
import pandas
import pandas as pds
import json
import sys
import mysql.connector
import datetime
from tabulate import tabulate


items = list(range(0, 200))
l = len(items)

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for items,tweet in enumerate(sntwitter.TwitterSearchScraper('#Macron since:2022-02-22 until:2022-02-23').get_items()):

    if items>l:
        break

    # Data to scrap
    tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.likeCount, tweet.replyCount, tweet.lang, tweet.coordinates, tweet.user.username])

    # Display percentage of advancement 
    percents=items*100/l
    sys.stdout.write("\r%d%%" % percents)
    sys.stdout.flush()

# Creating a dataframe from the tweets list above
tweets_df2 = pandas.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Reply Count', 'Like Count', 'Language', 'Coordinates', 'Username'])

# Creating a json from DataFrame (à améliorer avec la doc)
json_string = tweets_df2.to_json(orient="records")
parsed = json.loads(json_string)
test = json.dumps(parsed,indent=4)

tweets_df2 = pandas.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Reply Count', 'Like Count', 'Language', 'Coordinates', 'Username'])
#tweets_df2.style

df = pds.DataFrame(tweets_df2)
# Creating a json from DataFrame (à améliorer avec la doc)

print(tabulate(df, headers = 'keys', tablefmt = 'psql'))

f = open("data_loadbar.json","w")
f.write(test)
f.close()
