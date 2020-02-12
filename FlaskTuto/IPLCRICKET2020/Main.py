from calculation import *
#it will import only the summation() from calculation.py
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
r=ATI()
print("Sum = ",r.summation(a,b)) #we do not need to specify the module name while accessing summation()