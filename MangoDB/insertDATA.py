from pymongo import MongoClient

#Creating a pymongo client
client = MongoClient('localhost', 27017)

#Getting the database instance
db = client['mydb']

#Creating a collection
coll = db['example']

#Inserting document into a collection
# data =[
#    {
#       "_id": "101",
#       "name": "Ram",
#       "age": "26",
#       "city": "Hyderabad"
#    },
#    {
#       "_id": "102",
#       "name": "Rahim",
#       "age": "27",
#       "city": "Bangalore"
#    },
#    {
#       "_id": "103",
#       "name": "Robert",
#       "age": "28",
#       "city": "Mumbai"
#    }
# ]
# res = coll.insert_many(data)
# print("Data inserted ......")
# print(res.inserted_ids)
print("FIND RECOREDS ARE")
print(coll.find_one())
print(coll.find_one({"_id": "103"}))