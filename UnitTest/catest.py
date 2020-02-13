# def add(x,y):
#     return x+y
#
# def subtract(x,y):
#     return x-y
#
# def multiply(x,y):
#     return x*y
#
# def divide(x,y):
#     if y==0:
#         raise ValueError('Can not divided by zero!')
#     return x/y

import os
# h="cd /home/ravi/Documents/PYCODERS/UnitTest"
# s=os.system(h)
v=input()
ex="python {}.py".format(v)
ss=os.system(ex)
print(ss)
