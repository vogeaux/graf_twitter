import snscrape.modules.twitter as sntwitter
import pandas
import pandas as pds
import json
import sys
import mysql.connector
import datetime
from tabulate import tabulate

def scrapper(num_last=15):
    nombre_jour = 0
    items = list(range(0, 4000))
    l = len(items)


    #datetime.datetime.today()
    #todayday=datetime.datetime.today().strftime('%Y-%m-%d')
    #m=datetime.datetime.today().strftime('%Y-%m-')
    #d=int(datetime.datetime.today().strftime('%d'))-1
    #d=str(d)
    #yesterday=m+d

    num_last
    num = num_last+1

    num = str(num)
    num_last = str(num_last)

    yesterday ="2022-04-"+num_last+""
    todayday ="2022-04-"+num+""




    myCon=mysql.connector.connect(host='localhost',
                            database='data',
                            user='root',
                            password='mypass')




    mycursor = myCon.cursor()

    def insert(request_tweet_date="null",request_tweet_id="null",request_tweet_nombre_jour="null",request_tweet_content="null",request_tweet_like="null",request_tweet_user="null",request_tweet_name_politique="null"):
        sql = "INSERT INTO customers (time, id_tweet,nombre_jour, Text, likeCount, Username, name_politique) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (request_tweet_date,request_tweet_id,request_tweet_nombre_jour,request_tweet_content,request_tweet_like,request_tweet_user,request_tweet_name_politique)
        mycursor.execute(sql, val)

        myCon.commit()

        print(mycursor.rowcount, "record inserted.")


    # Creating list to append tweet data to
    tweets_list2 = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for items,tweet in enumerate(sntwitter.TwitterSearchScraper('#Macron since:'+yesterday+' until:'+todayday+' lang:fr').get_items()):

        if items>l:
            break

        # Data to scrap
        tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.likeCount, tweet.user.username])

        nombre_jour=nombre_jour+1

        name_politique1 = "Macron"
        request_tweet_like1=tweet.likeCount
        request_tweet_date1 = tweet.date
        request_tweet_id1 = str(tweet.id)
        print(request_tweet_id1)
        request_tweet_content1 = str(tweet.content)
        request_tweet_user1 = str(tweet.user.username)
        print(str(request_tweet_date1)+'///:::///'+request_tweet_user1)
        insert(request_tweet_date=request_tweet_date1,request_tweet_id=request_tweet_id1,request_tweet_nombre_jour=nombre_jour,request_tweet_like=request_tweet_like1,request_tweet_content=request_tweet_content1,request_tweet_user=request_tweet_user1,request_tweet_name_politique=name_politique1)

        # Display percentage of advancement 
        percents=items*100/l
        sys.stdout.write("\r%d%%" % percents)
        sys.stdout.flush()


    # Creating a dataframe from the tweets list above
    tweets_df2 = pandas.DataFrame(tweets_list2, columns=['time', 'id_tweet','likeCount', 'Text', 'Username, name_politique'])
    #tweets_df2.style

    df = pds.DataFrame(tweets_df2)
    # Creating a json from DataFrame (à améliorer avec la doc)

    print(tabulate(df, headers = 'keys', tablefmt = 'psql'))

    json_string = tweets_df2.to_json(orient="records")

    parsed = json.loads(json_string)

    test = json.dumps(parsed,indent=4)





    f = open("data_loadbar.json","w")
    f.write(test)
    f.close()


for i in range(1,30,1):
    scrapper(i)