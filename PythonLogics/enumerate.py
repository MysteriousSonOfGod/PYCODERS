# enumerate() Parameters
# The enumerate() method takes two parameters:
# iterable - a sequence, an iterator, or objects that supports iteration
# start (optional) - enumerate() starts counting from this number. If start is omitted, 0 is taken as start.






l=[0,1,2,3,4]
k=[4,5,6,7,8]
# print(tuple(enumerate(l)))
for i,j, in enumerate(l):
    print(i, j)
# for m,n in enumerate(k,1):
#     print(m,n)
