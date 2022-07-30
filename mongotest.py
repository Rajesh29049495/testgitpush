import pymongo
client = pymongo.MongoClient("mongodb+srv://raji:mongodb@raji.o1f2h7a.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"sudhanshu",
    "email":"sudh@123",
    "surname":"kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

