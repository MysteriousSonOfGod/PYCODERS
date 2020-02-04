# from array import *
# array1=array('i', [10,20])
# for i in array1:
#     print(i)
#
import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

res = collections.ChainMap(dict1, dict2)

# Creating a single dictionary
print(res.maps, '\n')
