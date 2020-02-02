d={1:"ravi",2:"ravi"}
for i in d:
    print(i)
for i,j in d.items():
    print(i,j)
import sys
print(sys.getsizeof(d))
l=[1,"ravi",2,"ravi"]
print(sys.getsizeof(l))
post=dict(message="ravi", Language="English")
print(post)
post["user_id"]=9
post["datetime"]="hjdsgkjhvjdhv"
print(post)
