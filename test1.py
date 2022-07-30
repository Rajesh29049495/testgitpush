"""connecting with the mongodb"""
import pymongo
client = pymongo.MongoClient("mongodb+srv://raje:mongodb@cluster0.olsfeog.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

#now will try to dump some data into it
d = {
    "name" : "sudhanshu",
    "email" : "sudh@123",
    "surname" : "kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
