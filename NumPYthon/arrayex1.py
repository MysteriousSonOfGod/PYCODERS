# #pip install numpy
import numpy as np
# # # print(np)
# # # print("hi")
# ravi='kal'
# a=np.array([1,2,3,4,5,6])
# r=[j for j in a]
# n=[1,2,3,4,5,'kal']
# m=iter(r)
# k=iter(n)
# rs=dict(zip(m,k))
# print(rs)
# l=[]
# k=['ravi','prasad','kalyan','ram','jan']
# # d={}
# for i in a:
#     l.append(i)
#
# it=iter(l)
# ls=iter(k)
# d=dict(zip(ls,it))
# print(d)

# l = [[1, 2, 3], [4, 5, 6], [7], [8, 9],[[[[[[[1,2,3,4,5,6,7,8]]]]]]]]
# e=[]
# ss=[]
# def rl(l):
#     for i in l:
#         if type(i) == list:
#             rl(i)
#         else:
#             e.append(i)
# rl(l)
# #USING DICTIONARY
# # e=list(dict.fromkeys(e))
# # print(e)
#
# print(list(set(e)))
# for i in list(set(e)):
#     print(i)
# m=["kalyani","ravi","prasad","kolli","sanaboina","ILOVE"]
# l=[1,2,3,3,4,4,5,555,5,5,5,5,5,5,]
# print(list(set(l)))
# n=iter(m)
# o=iter(list(set(l)))
# d=dict(zip(n,o))
# print(d)




# a = np.array([[1, 2], [3, 4], [5,6, [7,8]]])
# a = np.array([1, 2, 3,4,5], ndmin = 3)
# print(a)
# e=[]#EMPTY LIST FOR ARRY ELEMENT LIST
# nl=[]#EMPTY LIST FOR REMOVED DUPLICATE ELEMENTS IN THE array

# for i in a:
#     print(i)
#     e.extend(i)
# def rm(a):
#     for j in a:
#         if type(j)==list:
#             if type(j)=="array":
#                 rm(j)
#         else:
#             nl.append(j)
#
# rm(a)
# print(nl)


# a=np.array([[3,4,3],[5,6,7]])
# a.shape=(3,2)
# print(a)

#ARANGE THE AMOUNT
# a=np.arange(23)
# print(a)
# l=[1,2,3,4,5,6,7,8,24,26,27,28,29,10,12,13,14,15,16]
# n=iter(a)
# m=iter(l)
# rs=dict(zip(n,m))
# print(rs)


# a=np.arange(24)
# a.ndim
#
# b=a.reshape(2,4,3)
# print(b)




# x=[1,2,3,4,"ravi"]
# a=np.asarray(x)
# for i in a:
#     print(i)




a=np.arange(10)
print(a)
# s=slice(2,7,3)
# b=a[2:7:1]
# s=a[0]
print(a[::-1])
print(a[2:5])
print(np.char.add(['hello'],['prasad']))
print(np.char.split('ravi prasad'))