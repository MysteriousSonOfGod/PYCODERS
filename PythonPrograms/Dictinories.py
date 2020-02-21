from collections import ChainMap

l=[{
    "id":1, "data":"Happy"},
    {
        "id":2, "data":"Hungry"
}]
n=[]
m=[]
for i in l:
    for j,k in i.items():
        n.append(j)
        m.append(k)
print(n,m)
r=iter(n)
f=iter(m)
fin=dict(zip(r,f))
print(fin)