import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
mycol = mydb["datadb"]

mydict = { "name": "John", "address": "Highway 37" }

# x = mycol.insert_one(mydict)
x = mycol.find_one()

print(x)