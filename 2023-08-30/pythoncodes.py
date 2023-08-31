# CREATING FUNCTIONS USING def

# adding 2 no.s
# def add(num1,num2):
#     print(num1+num2)
# add(3,6)

# def high(a,b,c):
#     if a>b and a>c:
#         print("a is greatest")
#     elif b>a and b>c:
#         print("b is greatest")
#     else:
#         print("c is greatest")

# high(3,5,7)

# converting from kg to lbs
# def weight(a):
#     print(a*2.2)

# weight(30)

# converting from degree celcius to farhenheit
# def temp(a):
#     print(a*1.8+32)

# temp(10)

# return stmnt
# def fname(a,b):
#     sum=a+b
#     return sum
# print(fname(1,2))

# ARBITRARY ARGUMENTS
# def fname(*kids):
#     print("youngest kid is " + kids[-1])
# fname("tom","jerry","sam")

# def add1(*numbers):
#     print(sum(numbers))
# add1(1,2,3,123)

# keyword arguments
# def kids(first,second,third):
#     print(third+second+first)
# kids(third="tom ",first="jerry ",second="sam ")

# default parameter
# def nationality(country="India"):
#     print(country)
# nationality("USA")

# def age(age=18):
#     print("i am",age,"years old")
# age(21)
 
# recursion (to call function within function)
# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return(x*factorial(x-1))
# print(factorial(10))

# def hello():
#     print("hello")
#     hello()
# hello()

# ARBITRARY KEYWORD ARGUMENTS
# def fname(**person):
#     print("my name is "+person["name"])
# fname(name="peter",lastname="parker")

# lambda
# double=lambda x:x*2 where x is parameter and x*2 is expression
# hi=lambda x,y:x+y
# print(hi(3,2))

# lambda has mainly 3 functions:filter(),map(),reduce()
# filter()
# mylist=[1,5,4,3,2,8]
# newlist=list(filter(lambda x:(x%2==0),mylist))
# print(newlist)
    # to print even values from list
    # for filter function it should be inside list()

# mylist=[1,5,4,3,2,8]
# newlist=list(filter(lambda x:(x%2!=0),mylist))
# print(newlist)
    # to print odd values from list

# map()
# oldlist=[1,2,3,4]
# newlist=list(map(lambda x:(x*x*x),oldlist))
# print(newlist)

# reduce()
# from ast import Sub
# from functools import reduce
# li=[5,8,10,20,50,100]
# sum=reduce(lambda x,y:x+y,li)
# print(sum)