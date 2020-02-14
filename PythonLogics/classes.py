# class emp:
#     id=10
#     name="ravi"
#     def di(self):
#         print(self.id,self.name)
#
# e=emp()
# print(e.di())


#constructors
# class emp:
#     def __init__(self, name, id):
#         self.name=name
#         self.id=id
#     def dis(self):
#         print(self.name, self.id)
#
#
# e=emp("ravi",143)
# r=emp("prasad",455)
# e.dis()
# r.dis()
# class Student:
#     def __init__(self,name,age,id):
#         self.name=name
#         self.id=id
#         self.age=age
# s=Student("Ravi",25,12544)
# print(getattr(s,"name"))
# # print(getattr(s,"age"))
# print(getattr(s,"id"))
# setattr(s,"age",24)
# print(getattr(s,"age"))

# class Ram:
#     def __init__(self, name, age, id):
#         self.name=name
#         self.age=age
#         self.id=id
#
#     def di(self):
#         print(self.name,self.age,self.id)
#
# k=Ram("ravi",25,56546)
# d={}
# print(k.__doc__)
# print(k.__dict__)
# d.update(k.__dict__)
# for i,j in d.items():
#     print(i,j)
# print(k.__module__)
# print(k.__hash__())
# for i,j in k.__dict__.items():
#     print(i,j)


# class Animal:
#     def speak(self):
#         print("Animal Speaking")
#
# class Dog(Animal):
#     def bark(self):
#         print("Dog barking")
#
# d=Dog()
# d.speak()
# d.bark()


# class Calculator:
#     def Summation(self,a,b):
#         return a+b
#
# class Calculator1:
#     def Multiplication(self,a,b):
#         return a*b
#
# class Fi(Calculator,Calculator1):
#     def div(self,a,b):
#         return a/b
#
# r=Fi()
# print(r.Summation(2,3))
# print(r.Multiplication(20,6))
# print(r.div(10,2))

#
# class Cal:
#     def Summation(self,a,b):
#         return a+b
#
# class Cal1(Cal):
#     def Summation(self,a,b):
#         return a*b
#
# r=Cal1()
# print(issubclass(Cal1,Cal))

# Real
# Life
# Example
# of
# method
# overriding


# class Bank:
#     def getroi(self):
#         return 10;
#
#
# class SBI(Bank):
#     def getroi(self):
#         return 7;
#
#
# class ICICI(Bank):
#     def getroi(self):
#         return 8;
#
#
# b1 = Bank()
# b2 = SBI()
# b3 = ICICI()
# print("Bank Rate of interest:", b1.getroi());
# print("SBI Rate of interest:", b2.getroi());
# print("ICICI Rate of interest:", b3.getroi());


#DATA ABSTRACTION

class Employee:
    __count = 0;
    r=1
    def __init__(self):
        Employee.__count = Employee.__count+1
    def display(self):
        print("The number of employees",Employee.__count)
emp = Employee()
emp2 = Employee()
try:
    print(emp.r)
finally:
    emp.display()



































