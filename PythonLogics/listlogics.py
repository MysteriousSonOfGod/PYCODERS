# l=[1,2,3,4,5,5,5,6,6]
#REMOVE DUPLICATE ELEMENTS IN THE LIST
# r=list(set(l))
# print(r)

#INSERT ELEMENTS IN THE MIDDLE OF THE LIST
# l[2:3]=[7,8]
# print(l)

#COUNT NUMBER ELEMENTS WHICH IS REPEATED TWICE
# one=[(1),(1,),(1,1)]
# print(one.count(2))

# k=[]
# for i in range(0,100):
#     for j in l.count(i):
#         k
#
# print(k)


# l=[1,2,3,4,[2,3,4,[[[[[[[[[4,5,6,0000]]]]]]]]]]]
# e=[]
# def dl(l):
#     for i in l:
#         if type(i)==list:
#             dl(i)
#         else:
#             e.append(i)
#
# dl(l)
# print(e)

# from itertools import chain
# lst=[[5,6,8],[8,5,3],[7],[9,10,3],[3,5]]
# print(list(chain(*lst)))

# from functools import reduce
# from operator import add
# from itertools import accumulate
# lst=[[5,6,8],[8,5,3],[7],[9,10,3],[3,5]]
# print(reduce(lambda x,y:x+y, lst))
# print(reduce(add, lst))
# print(list(accumulate(lst))[-1])


# l=[154654,2,3,3,28588,1,2,3,11,11,111,11,1,1]
# e=[]
# # for i in l:
# #     if i not in e:
# #         e.append(i)
#
# r=[i for i in l if i not in e.append(i)]
# print(e)

# r=list(dict.fromkeys(l))
# print(r)


# r=set(l)
# print(list(r))
#
# l.sort()
# print(list(set(l)))


#
# i=list(range(1,10))
# print(i)
# s=list(filter(lambda x:x%2==0,i))
# print(sum(s))

# s=[]
# for i in range(1,101):
#     s.append(i**2)
# print(s)
#
#
# s1=[i**2 for i in range(1,100)]
# print(s1)
#
#
# HumanBodyParts=['Head','Hair','ear','Eye','Nose','chest','Neck','Stomach','Arm','Leg','Foot','ForeHead','Mouth','Lip','Chin','Nipple','Amdomen','Navel','Hip',
#                 'Groin','Leg','Thigh','Hand','Knee','Foot','Instep','Toenail','Armpit','Elbow','Waist','Wrist',
#                 'Thumb','Forearm','Fingers','Calf','Heal','Ankle','Shoulder','Temple','eyebrow','eyelash','iris','cheek','jaw','nostril','palm','index finger','littel finger','ring finger'
#                 ]
# aboy=[a for a in HumanBodyParts if a.startswith("H")]
# print(aboy)
# movies=[("Ravi",1992),("Kalyan",1994)]
# p=[i for (i,y) in movies if y <2000]
# print(p)
# Flowers=['Rose','Lotus','Marigold','Jasmine','Sunflower','Hibiscus','Mangnolia','Caldera','Basil','Lily Love','Lily Flower','Night Jaas','Promegranate']

# l=[1,2,3,4]
# b=[5,6,7,8]
# t=(1,2,3,4)
# for i in l:
#     for j in b:
#         print(i,j)
#
# r=[(i,j) for i in l for j in b]
# print(r)
# print(200*'-')
#
# print(150*'-')
# import sys
# print(dir(sys))
# print(150*'-')
# # print(help(sys))
# print("List Size",sys.getsizeof(l))
# print("Tuples Size",sys.getsizeof(t))
# r=tuple(l)
# print(r)
# print(sys.getsizeof(r))
#
# t=1,
# t2=2
# print(type(t))



# def ev(r):
#     return(if r%2==0:)
#
# l=[1,2,3,4,5,6,7,8]
# e=[]
# for r in l:
#     a=even(r)
#     e.append(a)
# print(e)

import statistics
data=[1,2,3,4,5,6,7,7]
avg=statistics.mean(data)
print(avg)

r=filter(lambda x:x>avg, data)
print(list(r))


l=["","ravi","","Kalyan"]
d=list(filter(None, l))
print(d)
# dd=list(filter( l))
# print(dd)
a=None
print("%s"%(a))