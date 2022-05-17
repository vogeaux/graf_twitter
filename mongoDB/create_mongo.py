import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
print(myclient.list_database_names())

mydb = myclient["mydatabase"]

#mydb = myclient["test"]

mycol = mydb["macron"]

#mydict = { "name": "John", "address": "Highway 37" }
mydict = { "time": "John", "id_tweet": "Highway 37", "nombre_jour": "Highway 37", "Text": "Highway 37", "likeCount": "Highway 37", "Username": "Highway 37", "name_politique": "Highway 37" }

x = mycol.insert_one(mydict)

print(mydb.list_collection_names())

x = mycol.find_one()

print(x)

