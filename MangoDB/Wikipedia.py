from pymongo import MongoClient

class Wikis:
    def __init__(self):
        self.myclient = MongoClient("localhost", 27017)
        self.mydb = self.myclient["mydb"]

    def ShowDB(self):
        return self.myclient.list_database_names()


    def ShowCollections(self):
        return self.mydb.list_collection_names()


    def CreateColl(self, n):
        self.cr=self.mydb.create_collection(n)
        return self.cr


    def Insert(self, mylist):
        emptylist = []
        temp = 0
        ran=len(mylist)
        import pdb
        pdb.set_trace()
        while temp < len(mylist):
            emptylist.append({mylist[temp]:mylist[temp+1]})
            temp+=2
        x = self.cr.insert_many(emptylist)
        return x


    def Find(self):
        x = self.mydb.csk.find()
        return x


EnglishWords= ['devastated', 'నాశనం', 'weird', 'అసహజ', 'embrace', 'ఆలింగనం', 'embarrassed', 'అసహనం', 'offend', 'నేరం']
result=Wikis()
s=result.ShowDB()
print(s)
c=result.ShowCollections()
print(c)
# print("---------------------Enter The Collection Name:-------------------")
# colname=input()
# result.CreateColl(colname)
# insertData=result.Insert(EnglishWords)
# print(insertData)
f = result.Find()
e=[]
for i in f:
    e.append(i)
print(e[2])
for k in e[2]:
    print(k)

