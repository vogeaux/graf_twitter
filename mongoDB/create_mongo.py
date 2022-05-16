import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
print(myclient.list_database_names())

mydb = myclient["mydatabase"]

#mydb = myclient["test"]

mycol = mydb["macron"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

print(mydb.list_collection_names())

x = mycol.find_one()

print(x)

