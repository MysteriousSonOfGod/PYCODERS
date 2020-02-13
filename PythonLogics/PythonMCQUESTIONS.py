#1.WHAT WILL BE THE OUTPUT OF THE FOLLOWING PROGRAMMING
# print(min("Hi python_scripts"))

#
import math
class Fact:
    def __init__(self):
        print("\nFACT IS")

    def __call__(self, no):
        facts=math.factorial(no)
        print("\n THE FACTORIAL OF "+str(no)+ ":"+str(facts))

if __name__=="__main__":
    n=int(input())
    f=Fact()
    f(n)
