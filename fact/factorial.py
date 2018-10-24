#!/usr/bin/env python3
#Author: James DuDasko

# Variables
x = int(input("Enter a number: "))
f = 1

#Factorial Loop
for i in range(1, x+1):
     f = f * i
print(str(x) + '! = ' + str(f))
