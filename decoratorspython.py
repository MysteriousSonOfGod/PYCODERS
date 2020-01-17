#A decorator is a design pattern in Python that allows a user to add new functionality
# to an existing object without modifying its structure.
# Decorators are usually called before the definition of a function you want to decorate

# def one(n):
#     return n+1
#
# add=one
# print(add(5))

#INSIDE ANOTHER FUNCTION
# def one(n):
#     def add_one(n):
#         return n+1
#
#     r=add_one(n)
#     return r
# print(one(5))


#Passing Functions as Arguments to other Functions
# def one(n):
#     return n+1
#
# def two(function):
#     nd=5
#     return function(nd)
#
# print(two(one))


# def sum(n):
#     return n+3
#
# def dis(function):
#     nd=10
#     return function(nd)
#
# print(dis(sum))

# def hf():
#     def i():
#         return "HI"
#     return i
#
# r=hf()
# print(r())



#Nested Functions have access to the Enclosing Function's Variable Scope

# def f(message):
#     def s():
#         print(message)
#
#
#     s()
#
#
# print(f("This is Ravi from Hyderabad"))







#Creating Decorators

# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#
#     return wrapper
#Applying Multiple Decorators to a Single Function
#We can use multiple decorators to a single function. However, the decorators will be applied in the order that we've called them.
#Below we'll define another decorator that splits the sentence into a list.
#We'll then apply the uppercase_decorator and split_string decorator to a single function.

# def split_string(function):
#     def wrapper():
#         func = function()
#         splitted_string = func.split()
#         return splitted_string
#
#     return wrapper
#
# @split_string
# @uppercase_decorator
# def say_hi():
#     return 'hello there'
#
#
# # decorate = uppercase_decorator(say_hi)
# # decorate()
# print(say_hi())




def fupper(function):
    def warpper():
        func=function()
        fp=func.upper()
        return fp


    return warpper


def sp(function):
    def wrapper():
        func=function()
        st=func.split()
        return st


    return wrapper

@sp
@fupper
def dis():
    return "Kalyani Ravi"

# d=fupper(dis)
print(dis())
































































