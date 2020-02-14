import array as arr
a=arr.array('i',[2,3,4,5,6])
# print(a)
for i in a:
    print(i)
a[2:4]=arr.array('i',[88,98,108])
k=[]
for j in a:
    k.append(j)
print(k)