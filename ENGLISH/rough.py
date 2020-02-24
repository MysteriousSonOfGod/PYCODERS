l=[1,'kal',2,'ravi',3,'ram']
p=[]
t=0
while t < len(l):
    for i in range(1, int(len(l)/2)):
        p.append({l[t]:l[t+1]})
        t=t+2
print(type(p))
