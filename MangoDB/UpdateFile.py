from pymongo import MongoClient

#Creating a pymongo client
client = MongoClient('localhost', 27017)

#Getting the database instance
db = client['myDB']

#Creating a collection
coll = db['example']

#Inserting document into a collection
# data = [
#    {"_id": "101", "name": "Ram", "age": "26", "city": "Hyderabad"},
#    {"_id": "102", "name": "Rahim", "age": "27", "city": "Bangalore"},
#    {"_id": "103", "name": "Robert", "age": "28", "city": "Mumbai"}
# ]
# res = coll.insert_many(data)
# print("Data inserted ......")

#Retrieving all the records using the find() method
print("Documents in the collection: ")
for doc1 in coll.find():
    print(doc1)
coll.update_one({"_id":"102"},{"$set":{"city":"Visakhapatnam"}})

#Retrieving all the records using the find() method
print("Documents in the collection after update operation: ")

for doc2 in coll.find():
   print(doc2)