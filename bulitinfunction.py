# l=['1+20', '2+8', '8+9']
# print(list(map(eval, l)))
# print(eval('1+2'))

# def f(n):
#     return len(n)
#
# x=map(f,['ravi'])
# print(x)
# print(list(x))



#MAP
# def calculateSquare(n):
#   return n*n
#
# numbers = (1, 2, 3, 4)
# result = map(calculateSquare, numbers)
# print(result)
#
# # converting map object to set
# numbersSquare = set(result)
# print(numbersSquare)




#Example 2: How to use lambda function with map()?

# numbers = (1, 2, 3, 4)
# result = map(lambda x: x*x, numbers)
# print(result)
#
# # converting map object to set
# numbersSquare = set(result)
# print(numbersSquare)



# n=[1,2,3,4,5,6]
# r=map(lambda x: x*x, n)
# print(r)
# ns=list(r)
# print(ns)





# from operator import add
# l=[1,2,3,4]
# l2=[5,6,7,8]
# r=map(lambda n1, n2:n1+n2, l,l2)#TWO LIST ADDING USING MAP AND LAMBDA FUNCTION
# print(list(r))
# print(l+l2)
# e=[]
# for i in range(0,len(l)):
#     e.append(l[i]+l2[i])
# print(e)
#
# k=[l[i]+l2[i] for i in range(len(l))]
# print(k)
# print(list(map(add, l, l2)))
# t=[sum(i) for i in zip(l,l2)]
# print(t)

# l=[1,2,3,4]
# l2=[1,2,3,4]
# r=map(lambda a,b:a+b, l,l2)
# print(list(r))
# t=[sum(i) for i in zip(l,l2)]
# print(t)


# l = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
# e=[]
# for i in  l:
#     for j in i:
#         e.append(j)
#
# print(e)

# l=[[1,2,3],[[[[[[2,3,4,5,6,6]]]]]]]
# e=[]
# def rl(l):
#     for i in l:
#         if type(i) == list:
#             rl(i)
#         else:
#             e.append(i)
#
# rl(l)
# print(e)
#
# l=[[[[[[[[[[[[[[[[[[[[1,2,3,3,4,5,],3,4,5,6,7,77,7,7,7,7,7,7,7,7,7,777,7,7,7,7,7]]]]]]]]]]]]]]]]]]]
# e=[]
# def rl(l):
#     for i in l:
#         if type(i)==list:
#             rl(i)
#         else:
#             e.append(i)
#
# rl(l)
# print(e)


# t=((((2,4),5,6)),(8,5))
# e=[]
# # for i in t:
# #     for j in i:
# #         e.append(j)
# def tp(t):
#     for i in t:
#         if type(i)==tuple:
#             tp(i)
#         else:
#             e.append(i)
#
# tp(t)
# print(tuple(e))

# t=((1,3),1,3,(1,3,(1,3),1,3),1,3)
# e=[]
# def tr(t):
#     for i in t:
#         if type(i)==tuple:
#             tr(i)
#         else:
#             e.append(i)
# tr(t)
# print(tuple(e))



s={"ravi",2,3,4,"ravi"}
e=[]
print(s)
def dl(s):
    for i in s:
        if type(i)==set:
            dl(i)
        else:
            e.append(i)
dl(s)
print(set(e))










