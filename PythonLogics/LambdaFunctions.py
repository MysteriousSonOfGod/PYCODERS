# r=full_name=lambda fn, ln: fn.strip().title()+" "+ln.strip().title()
# print(r("  Ravi peasad","KALYAN"))
#
# s = set("Hacker")
# print (s.symmetric_difference("Rank"))
# set(['c', 'r', 'e', 'H'])



# n=int(input())
# e=[]
# for i in range(n):
#     j=int(input())
#     e.append(j)
#
# print(e)




#
# firstnum = int(input())
# first_set = set(map(int, input().split()))
# secondnum = int(input())
# second_set = set(map(int, input().split()))
#
# print (len(first_set.symmetric_difference(second_set)))

# H=set("Hacker")
# R=set("Rank")
# H.update(R)
# print(H)
# LA = input()
# A = set(map(int,input().split()))
#
# N = int(input())
#
# for i in range(N):
# 	k = input().split()
# 	ktemp = set(map(int,input().split()))
# 	if k[0] == 'update':
# 		A.update(ktemp)
# 	elif k[0] == 'intersection_update':
# 		A.intersection_update(ktemp)
# 	elif k[0] == 'difference_update':
# 		A.difference_update(ktemp)
# 	elif k[0] == 'symmetric_difference_update':
# 		A.symmetric_difference_update(ktemp)
# 	else:
# 		print ('Incorrect parameters')
#
# r=list(A)
# s=sum(r)
# print(s)


# from collections import Counter
#
# n = input()
# b = input().split()
#
# k = Counter(b)
# d = dict(k)
#
# print(min(d, key=lambda k: d[k]))
# 
# for i in range(int(input())):
#     a = int(input())
#     A = set(input().split())
#     b = int(input())
#     B = set(input().split())
#     if A.issubset(B) :
#         print('True')
#     else :
#         print('False')
        



# s="ravi"
# e=""
# for i in s:
#     for j in range(2):
#         e+=i
# print(e)


# import statistics
# l=[1,2,3,4,5,6,7,8]
# avg=statistics.mean(l)
# r=filter(lambda x:x>2, l)
# print(list(r))
#
# d={1:"ravi", 2:"prasad", 3:"kalyan", 4:"prasad"}
# print(d)
# for i in d.values():
#     for j in d.keys():
#         if d.values()==i:
#             print(j)

# list = [1, 7, 8, 4, 5, 3]
#
# for x, y in zip(list[::], list[1::]):
#     print(x, y)

#
# mylist = [1,2,3,4,5,6,7,8,9]
# for i in range(len(mylist)):
#     # do something special in case of i = 0
#     # do something special in case of i = len(mylist)
#     prev = mylist[i-1]
#     cur = mylist[i]
#     nxt = mylist[i+1]
#     # do something with the three values


# mylist = ["A", "B", "C", "D", "E"]
#
# for i, element in enumerate(mylist):
#     previous_element = mylist[i - 1] if i > 0 else None
#     current_element = element
#     next_element = mylist[i + 1] if i < len(mylist) - 1 else None
#     print(previous_element, current_element, next_element)


# Python program to find second largest
# number in a list

# list of numbers - length of list should be at least 2
list1 = [10, 20, 4, 45, 45, 99]

max=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])

for i in range(2,len(list1)):
	if list1[i]>max:
		secondmax=max
		max=list1[i]
	else:
		if list1[i]>secondmax:
			secondmax=list1[i]

print("Second highest number is : ",str(secondmax))
