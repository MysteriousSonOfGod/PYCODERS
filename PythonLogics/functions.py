# def ravi():
#     print("jhdjhv")
#
# def s(a,b):
#     return a+b
# def p(*names):
#     for i in names:
#         print(i)
#
# a=10
# b=222
# ravi()
# print("sum is",s(a,b))
# p("ravi","prasad",'sanaboina0',3,4)\

# l=[1,2,3,4]
# print(sum(l))
# x=lambda a:a+10
# print(x(20))


#----------------------------------------------------------------------------------------------------------------------
class C:
    count=2
    def __init__(self,a):
        self.count+=1
        self.a=a
        print(self.a)
ins=[C(i) for i in range(10)]
import pdb
pdb.set_trace()
print(C.count)