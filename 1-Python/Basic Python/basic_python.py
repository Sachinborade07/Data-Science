#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 09:36:15 2024

@author: Sachin Borade
"""

# First line of code
print("Hello")

# Variable
''' 
Types of Numbers
There are three types used to represent numbers in python;
these are integers (or integral) types,
floating point numbers and complex numbers;
'''

x = 1
print(x)
print(type(x)) #it will take int as by default

x = 10.7
print(x)
print(type(x)) #it will take float as by default 

x = 10000000000000000000000000000000000007
print(x)
print(type(x)) #it wi=ll take int for any size of integer


''' 
    The input() function always return a string 
    If we want ot ask the user to input an integer number, then
    we will need ot convert the string returened form the input() 
    function to an int.
    We can do this by wrapping the call to the input()
    function in a call to the int() function
'''

age = input("Enter your age:")
print(type(age))
print(age)
# It is going to be by default string 


age1 = input("Enter age1:-")
print(type(age1))

age2 = input("Enter age2:-")
print(type(age2))

age = age1 + age2

print(age)
print(type(age))


age1 = int(input('Enter age1:- '))
print(age1)

age2 = int(input("Enter age2:-"))
print(age2)

age = age1 + age2
print(age)
# The specific resutl we want 

#################################################################
'''
    Floating point numebers,
    Real number 
    are represented in Python using IEEE 75
    double-precision binary floating-point number
'''
exchange_rate = 1.93
print(exchange_rate)
print(type(exchange_rate))
#################################################################
#converting to floats
#as with integers it is possible to convert other types 
#such as an int or a string into a float
int_value = 100
string_value = '1.5'

float_value = float(int_value)
print("Int value as a float:-",float_value)

float_value = float(string_value)
print("string value as a float:-",float_value)
print(type(float_value))

#################################################################

#Complex Numbers
c1 = 1
c2 = 2j
print("c1:-",c1)
print("c2:-",c2)

#complex number1
print(c1.real)
print(c1.imag)

#complex number2
print(c2.real)
print(c2.imag)

#################################################################

#Boolean Values
# Python supports another type called Boolean
# A boolean type can only be one of True or False

all_ok = True
all_notok = False
print(all_ok)
print(all_notok)
print(type(all_ok))
print(type(all_notok))

#################################################################

# You can also convert strings into Boolean as 
# True ro False (and nothing else)

status = bool(input("Ok it is confirmed :-"))
print(status)
print(type(status))

#################################################################

# Arithmetic Operators 

'''
    Arithmetic operaters are used to perform 
    some form of mathematical operation such 
    addition, subtraction ,multiplication 
    and division etc.
    In python they are represented by one or two
    characters.
'''

home = 10
away = 14
print(home + away )
print(type(home + away))
# After performing operation the type will be int

print(10 * 4)
print(type(10 * 4))
# After performing operation the type will be int 

print(10 - 4)
print(type(10 - 4))
# After performing operation the type will be int

#################################################################

'''
 However we have missed out division with respect to integers,
 why is this ?
 It is because it depends on which division operator you use as
 to what the returned type actually is. 
 e.g. If we divide the integer 100 by 20 then the result you 
 might reasonably expect to produce might be 5
 but it is not 5 it is 5.0
'''


#################################################################
''' To ignore the fractional part then
    there is an allternative version of the 
    divide operator // (floor) division'''

print(100//20)
print(type(100//20))

'''interested in reminder'''

print('Modulus division 100 %m3:',100%3)
print('modulus division 3%2:',3%2)

'''to calculate power we are using **'''

a = 5
b = 3
print(a**3)

#################################################################

#Assignment operator
x = 0
x += 1
print(x)

#################################################################

#None value 
#python has a special type,
#the NoneType, with a single value, None.
winner = None
print(winner is None)

print(winner is not None)

winner = None
print('winner:', winner)
print('winner is None:',winner is None)
print('winner is not None:',winner is not None)
print(type(winner))

#################################################################

#flow of control using If statement
#Comparison Operators

num = int(input("Enter a number : "))
if num > 0:
    print(num)
    
#Else in an If statement
num = int(input("Enter yet another number:"))
if num < 0:
    print("its negative")
else:
    print("its not negative")


#The use of elif
savings = float(input("enter your savings"))
if savings == 0:
    print("Sorry no savings")
elif savings < 500:
    print('Well done')
elif savings < 1000:
    print('Thats a tidy sum')
elif savings < 10000:
    print('Welcome sir')
else:
    print('Thank You')
    
#################################################################

#Iteration / Looping
#while loop
count = 1
print('Starting')
while count <= 10:
    print(count)
    count+=1
    
#################################################################

#for loop
#loop over a set of values in range
print('Print out values in a range')
for i in range(2,10):
    print(i)
    print('Done')
    
#################################################################
  
print("Only print code if all iterations completed")
num = int(input('Enter a number to check for:'))
for i in range(0,16):
    if i == num:
        break
    print(i)
print('Done')

#################################################################

#Now use an 'anonymous' loop variable
for _ in range (0,10):
    #print('.')
    print('.',end='')
    print()
    print(id(_))


#################################################################


# Python program to print odd numbers in given range

start , end = 1, 19

# Iterating each number in list
for num in range(start, end+1):
    # Checking condition 
    if num % 2 != 0:
        print(num, end=" ")
        

#################################################################

# To check whether the number is even or not 

n = int(input("Enter the number:-"))
for i in range(1,n+1):
    if i % 2 == 0:
        print(i,end=" ")

#################################################################

