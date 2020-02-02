# d={1:"ravi",2:"ravi"}
# for i in d:
#     print(i)
# for i,j in d.items():
#     print(i,j)
# import sys
# print(sys.getsizeof(d))
# l=[1,"ravi",2,"ravi"]
# print(sys.getsizeof(l))
# post=dict(message="ravi", Language="English")
# print(post)
# post["user_id"]=9
# post["datetime"]="hjdsgkjhvjdhv"
# print(post)

import json
f=open('jsonformat.json','r')
r=json.load(f)
dictlist=[]
for key, value in r.items():
    temp = [key,value]
    dictlist.append(temp)

print(dictlist)
e=[]
for i in dictlist:
    e.append(i)

print(e)
kl=[]
def rm(e):
    for j in e:
        if type(j)==list:
            rm(j)
        else:
            kl.append(j)
rm(e)
print(kl)
# l=list(r.items())
# print(l)
# for i in f:
#     print(i)
