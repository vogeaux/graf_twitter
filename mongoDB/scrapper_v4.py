from pickle import NONE
import snscrape.modules.twitter as sntwitter
import pandas
import pandas as pds
import json
import sys
import mysql.connector
import datetime
from tabulate import tabulate
import pymongo


def scrapper(num_last="NONE",nom_candidat="NONE"):
    nombre_jour = 0
    items = list(range(0, 10))
    l = len(items)


    #datetime.datetime.today()
    #todayday=datetime.datetime.today().strftime('%Y-%m-%d')
    #m=datetime.datetime.today().strftime('%Y-%m-')
    #d=int(datetime.datetime.today().strftime('%d'))-1
    #d=str(d)
    #yesterday=m+d

    # pour faire les 30 jours du mois 04

    num = num_last+1
    num = str(num)
    num_last = str(num_last)
    yesterday ="2022-04-"+num_last+""
    todayday ="2022-04-"+num+""




    # connection dans la db mongodb localhost
    # on peut voir les données avec compassdb
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    print(myclient.list_database_names())

    mydb = myclient["mydatabase"]

    mycol = mydb[nom_candidat]




    def insert(request_tweet_date="null",request_tweet_id="null",request_tweet_nombre_jour="null",request_tweet_content="null",request_tweet_like="null",request_tweet_user="null",request_tweet_name_politique="null"):


        mydict = { "time": request_tweet_date, "id_tweet": request_tweet_id, "nombre_jour": request_tweet_nombre_jour, "Text": request_tweet_content, "likeCount": request_tweet_like, "Username": request_tweet_user, "name_politique": request_tweet_name_politique }
        x = mycol.insert_one(mydict)
        x = mycol.find_one()



    # liste pour inport dans la variable
    tweets_list2 = []

    # Utilisation de TwitterSearchScraper pour récupérer des données et ajouter des tweets à la liste
    for items,tweet in enumerate(sntwitter.TwitterSearchScraper(''+nom_candidat+' since:'+yesterday+' until:'+todayday+' lang:fr').get_items()):

        if items>l:
            break

        # recup la Data avec la lib
        tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.likeCount, tweet.user.username])

        nombre_jour=nombre_jour+1

        name_politique1 = nom_candidat
        request_tweet_like1=tweet.likeCount
        request_tweet_date1 = tweet.date
        request_tweet_id1 = str(tweet.id)
        request_tweet_content1 = str(tweet.content)
        request_tweet_user1 = str(tweet.user.username)

        print(request_tweet_id1)
        print(str(request_tweet_date1)+'///:::///'+request_tweet_user1)


        insert(request_tweet_date=request_tweet_date1,request_tweet_id=request_tweet_id1,request_tweet_nombre_jour=nombre_jour,request_tweet_like=request_tweet_like1,request_tweet_content=request_tweet_content1,request_tweet_user=request_tweet_user1,request_tweet_name_politique=name_politique1)

        # Display percentage of advancement 
        percents=items*100/l
        sys.stdout.write("\r%d%%" % percents)
        sys.stdout.flush()


    # mise en forme
    tweets_df2 = pandas.DataFrame(tweets_list2, columns=['time', 'id_tweet','likeCount', 'Text', 'Username, name_politique'])

    df = pds.DataFrame(tweets_df2)
    # creation du json 

    print(tabulate(df, headers = 'keys', tablefmt = 'psql'))

    json_string = tweets_df2.to_json(orient="records")

    parsed = json.loads(json_string)

    test = json.dumps(parsed,indent=4)





    f = open("data_loadbar.json","w")
    f.write(test)
    f.close()



list1 = ["#Arthaud",
"#Roussel",
"#Macron",
"#Lassalle",
"#LePen",
"#Zemmour",
"#Melenchon",
"#Hidalgo",
"#Jadot",
"#Pecresse",
"#Poutou",
"#Dupont-Aignan"]

#blouque pour la liste qui est au dessus

#blouque pour la les nombre de jours

for a in list1:
    print(a)
    for i in range(1,30,1):
        scrapper(num_last=i,nom_candidat=a)