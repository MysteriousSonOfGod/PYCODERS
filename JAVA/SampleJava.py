import os
import time
import datetime

start_time = time.time()
n=input("Enter The File Name")
cmd="javac {}.java".format(n)
exe="java {}".format(n)
s=os.system(cmd)
s2=os.system(exe)
print("--- %s seconds ---" % (time.time() - start_time))
t=time.asctime()
# g=time.localtime()
print(t)
# print(g)
