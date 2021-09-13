#!/usr/bin/env python
# coding: utf-8

# # To find numbers between 2000 and 3200 which are divisible by 7 and not a multiple of 5

for i in range(2000,3200):
    if i%7 == 0 and i%5 != 0:
        print(i,end=',')


# # To accept the user's first name and last name and print them in the reverse order

x = input("enter first name")
y = input("enter last name")
print(x,y)
print((x +' '+ y)[::-1])


# # To find the volume of a sphere

r = 6
pi = 3.14159
v = 4/3 * pi * r ** 3
print(v)







