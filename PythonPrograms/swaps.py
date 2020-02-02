# a=10
# b=20
# # a,b=b,a #SIMPLE LOGIC FOR SWAP TWO NUMBERS
# print(a,b)
# t=a
# a=b
# b=t
# print(a,b)


#1.Python program to find the area of a triangle
# a=20#Enter first side
# b=20#Enter second side
# c=10#Enter Third side
# # print(a**b)
# s=(a+b+c)/2
# area=(s*(s-a)*(s-b)*(s-c))**0.5
# print(area)


#2.Python program to solve quadratic equation
#ax2+bx+c
# import cmath
#
# a = float(input('Enter a: '))
# b = float(input('Enter b: '))
# c = float(input('Enter c: '))
#
# # calculate the discriminant
# d = (b ** 2) - (4 * a * c)
#
# # find two solutions
# sol1 = (-b - cmath.sqrt(d)) / (2 * a)
# sol2 = (-b + cmath.sqrt(d)) / (2 * a)
# print('The solution are {0} and {1}'.format(sol1, sol2))


#3.PYTHON PROGRAM CONVERT KILOMETERS TO MILES
#1 kilometer is equal to 0.62137 miles.
# k=8
# # conversion factor
# conv_fac = 0.621371
# # Miles = kilometer * 0.62137
# # Kilometer = Miles / 0.62137
# miles=k*conv_fac
# print("{} Kilometers is equal to {}".format(k,miles))



#4.PYTHON PROGRAM CONVERT CELSIUS TO FAHRENHEIT
#T(℉) = T(℃) x 1.8 + 32
# celsius=37
# fahrenheit=(celsius * 1.8) + 32
# print("%0.1f Celsius is equal to %0.1f degree Fahrenheit"%(celsius,fahrenheit))



#5.GENERATE RANDOM NUMBERS
# import random
# print(random.randint(165276, 965276))

#6.CALENDAR
# import calendar
# print(calendar.month(1992,12))

#7.CHECK POSITIVE OR NEGATIVE NUMBER
# a=-9
# if a>=0:
#     print("NUMBER IS POSITIVE")
# else:
#     print("THE NUMBER IS NEGATIVE")

#8.PYTHON PROGRAM CHECK WHETHER NUMBER IS EVEN OR ODD

# a=11
# if (a%2==0):
#     print("THE NUMBER IS EVEN")
# else:
#     print("THE NUMBER IS ODD")

#9.PYTHON PROGRAM WHETHER THE YEAR IS LEAPYEAR OR NOT

# year=2016
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("YEAR IS LEAP YEAR")
#         else:
#             print("IS NOT A LEAP YEAR")
#     else:
#         print("THE YEAR IS LEAP YEAR")
# else:
#     print("THE YEAR IS NOT A LEAP YEAR")


#10.PYTHON PROGRAM TO CHECK WHETHER THE NUMBER IS PRIME OR NOT
# a=11
# if a>1:
#     for i in range(2,a):
#         if a%2==0:
#             print(a,"IS NOT A PRIME NY")
#             break
#     else:
#         print("NUMBER IS PRIME")
# else:
#     print("IS not prime")

#PRINT ALL PRIME NUMBERS IN THE GIVE LOWER RANGE TO UPPER RANGE
# l=10
# u=100
# for a in range(l, u+1):
#     if a > 1:
#         for i in range(2, a):
#             if a % 2 == 0:
#                 break
#         else:
#             print(a)



#11.WRITE A PYTHON PROGRAM FACTORIAL
# What is factorial?
#
# Factorial is a non-negative integer. It is the product of all positive integers less than or equal to that number for which you ask for factorial.
# It is denoted by exclamation sign (!).
# n=23
# f=1
# if n<=0:
#     print("THE NUMBER DOES NOT SUPPORT FACTORAL OPERATION")
# else:
#     for i in range(1,n+1):
#         f=f*i
#     print(f)


#NOTE cmath — Mathematical functions for complex numbers. This module is always available.
# It provides access to mathematical functions for complex numbers.
# The functions in this module accept integers, floating-point numbers or complex numbers as arguments.
#USING MATH FUNCTION
# import math
# print(math.factorial(-5))
# print(math.fabs(23.60000))



#12.MULTIPLICATION TABLE
# n=5
# for i in range(1,11):
#     print(i,"x",n,"=",n*i)



#13.Fibonacci Series Number
# nterms=10
# n1 = 0
# n2 = 1
# count = 2
# if nterms <= 0:
#    print("Plese enter a positive integer")
# elif nterms == 1:
#    print("Fibonacci sequence:")
#    print(n1)
# else:
#    print("Fibonacci sequence:")
#    print(n1,",",n2,end=', ')
#    while count < nterms:
#        nth = n1 + n2
#        print(nth,end=' , ')
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1




#14.For example: 153 is an Armstrong number since 153 = 1*1*1 + 5*5*5 + 3*3*3.
# n=153
# sum=0
# temp=n
# while temp>0:
#     di=temp%10
#     sum=sum+di**3
#     temp//=10
# if n==sum:
#     print("THE NUMBER IS AMSTRONG NUMBER")
# else:
#     print("THE NUMBER IS NOT A AMSTRONG NUMBER")


#15. SUM OF THE N NATURAL NUMBERS
# n=10
# sum=0
# while(n>0):
#     sum+=n
#     print(sum)
#     n-=1
# print(sum)



#16. LCM of two numbers
def gcd(x,y):
    if x==0:
        return y
    return gcd(y%x, x)


def lcm(x,y):
    return (x*y)/gcd(x,y)

x=8
y=20
print(lcm(x,y))

# a=12
# b=20
# c=a*b
# print(c)
# d=int(c/a)
# print(d)
# e=int(c/b)
# print(e)
