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

#--------------------------------------------Convert Single List to number of dictionaries------------------------------
# print("---------------------------MongoDB uses the list of dictionaries--------------------------")
# l=[1,'kal',2,'ravi',3,'ram']
# p=[]
# t=0
# while t < len(l):
#     p.append({l[t]:l[t+1]})
#     t=t+2
# print(p)

#--------------------------------------------