#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:33:14 2024

@author: Sachin Borade
"""
numerator = 50
divide = 0
quotient = (numerator/divide)
print(quotient) 
# ZeroDivisionError: division by zero
# For such a type of error we use exception handling as below


## Exception Handling 
try:
    numerator = 50
    divide = int(input("Enter the denomenator:-"))
    quotient = (numerator/divide)
    print(quotient)
    print("Division performed succesfully")
except:
    print("Oh, this is divide by zero error ")
print("We are out of Try and Except block")

## Now we can see there no error


try:
    numerator = 50
    denom = int(input("Enter the denominator:-"))
    print(numerator/denom)
    print("Division performed successfully")
except ZeroDivisionError:
    print("Denominator is Zero")
except ValueError:
    print("Only Integers should be entered")
    
    
try:
    numerator = 50
    denom = int(input("Enter the denominator:-"))
    print(numerator/denom)
    print("Division performed successfully")
except ValueError:
    print("Only Integers should be entered")
except:
    print("Opp's Some exception raised ")
    


    
    ## Handling exception using try....except....else
    
try:
    numerator = 50
    denom = int(input("Enter the denominator:-"))
    quotient = numerator / denom
    print("Division performed successfully")
except ZeroDivisionError:
    print("Denominator is Zero")
except ValueError:
    print("Only Integers should be entered")
else:
    print("The result of division operation is:",quotient)
    
    
    ## Handling exception using try...except...else...finally

try:
    numerator = 50
    denom = int(input("Enter the denominator:-"))
    quotient = numerator / denom
    print("Division performed successfully")
except ZeroDivisionError:
    print("Denominator is Zero")
except ValueError:
    print("Only Integers should be entered")
else:
    print("The result of division operation is:",quotient)
finally:
    print("OVER AND OUT")    
     
    