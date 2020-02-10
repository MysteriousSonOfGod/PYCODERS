# def func1(a,b):
#     print(a+b)
#
# func1(2,3)
# fun2=func1
# fun2(4,5)

# def add(x):
#     return x+1
# def sub(x):
#     return x-1
#
# def ope(func, x):
#     te=func(x)
#     return te
#
# print(ope(add, 10))
# print(ope(sub, 10))


#@decorator

def out_fu(func):
    def inner(x,y):
        if(x<y):
            x,y=y,x
            return func(x,y)

    return inner

@out_fu
def div(x,y):
    print(x/y)

@out_fu
def adds(f,y):
    print(f+y)
adds(1,2)