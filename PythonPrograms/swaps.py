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


#PYTHON PROGRAM TO CHECK WHETHER THE NUMBER IS PRIME OR NOT
a=11
if a>1:
    for i in range(2,a):
        if a%2==0:
            print(a,"IS NOT A PRIME NY")
            break
    else:
        print("NUMBER IS PRIME")
else:
    print("IS not prime")





