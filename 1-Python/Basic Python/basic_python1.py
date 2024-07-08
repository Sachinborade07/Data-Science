#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:28:48 2024

@author: Sachin Borade
"""

x,y,z = 4,5,6
print(x)
print(y)
print(z)

x,y,z = 5
 # TypeError: cannot unpack non-iterable int object
 # It will get TypeError because one number cannot be assigned to 
 # many variable at time
print(x)
print(y)
print(z)


#################################################################

# Global Variable 
x = "Awsome"
def my_function():
    print("Python is "+x)
my_function()

#################################################################

# Global and Local Variable 
x = "awsome"
def my_function():
    x = "fantastic"
    print("Python is "+x)
my_function()
print("Python is "+x)

#################################################################

#####   Checking the type of data ############

x = 5
print(type(x)) # <class 'int'>

x = range(6)
print(type(x)) # <class 'range'>

x = {"name":"sachin","age":20}
print(type(x)) # <class 'dict'>

x = [1,2,3]
print(type(x)) # <class 'list'>

x = (1,2,3)
print(type(x)) # <class 'typle'> 

#################################################################
# assigning values
x = 1
print(type(x))
y = 2,3
print(type(y))
z = 2 + 3j
print(type(z))

x = 1
z = float(x)
print(type(z))

#################################################################

#################### String Operations ##########################

str1 = "hello"
str2 = 2
str3 = str1 + str2
# TypeError: can only concatenate str (not "int") to str
# It will give us error as string is not going to concatnate with 
# the integer value 

# String
# If you want multiple strings
x = '''This is python. It is very powerful '''
print(x)

# String Slicing
x = '''This is python. It is very powerful'''
print(x[2:8])

# Slicing string from start to specific point 
print(x[:4])

# Slice to the end form a specific point
print(x[4:])

# Negative Indexing 
print(x[-5:-2])

print(x[-5:2:-1])


# Modification of String 
# to lower ot upper and upper to lower

# Lower Case
x = x.lower()
print(x)

# Upper Case
x = x.upper()
print(x)

################# Remove spaces from initially ##################

x = "   This is python   "
print("The length before removing spaces",len(x))
x = x.strip()
print("The length after removing spaces",len(x))
print(x)


################# Replacing the words in python #################

x = " Hello World "
x = x.replace("Hello","Gello")
print(x)
# It will replace "Hello" with "Gello"


########## Seperating string into words based on space ##########

x = "Hello World"
print(x.split(" ")) # ['Hello', 'World']
# The words are getting seperated based on space into string

x = "Hello ,World"
print(x.split(","))


#### Reverse the string ######
#String 
x = "hello world"
string1 = x[::-2]
print(string1)

reversed_string = x[::-1]
print(reversed_string)


#################################################################

#Find method
# Searches the string for a specified value 

x = "This is python and it is very powerful"
print(x.find("and")) #It will give us location of specific word


## String Concateness ##
x = "hello"
y = "world"
print(x+y)
##########
# To add white space
print(x+" "+y)

#################################################################

# String format 
x = 20
y = "My name is Sachin "
print(x + y) #error (we cannot concatenate the string and integer)

# So we need  the output in below fashion.
print(f"{y} and my age is {x}")

quantity = int(input("Enter the quantity"))
item_no = int(input("Enter item number"))
price = int(input("Enter the price"))
print(f"I want {quantity} pieces and item number is {item_no} and its price is {price} ")

# String empty format
quantity = 20
item_no = 30.2
price = 2
my_order = "I want {} pieces and item number is {}, its price is {} "
print(my_order.format(quantity,item_no,price))


# We can also give the id number to the breaces 
quantity = 20
item_no = 30.2
price = 200
my_order = "I want {0} pieces and item number is {1}, its price is {2} "
print(my_order.format(quantity,item_no,price))

# If I want to write a string inside the string 
text = "This is fun and fair for "us" " 
# after printing the text it is going to give me error
# To remove error we use
text = "This is fun and fair for \"us \" "
print(text) # Now it is not going to give us the error


#################################################################


# Python Operator 

a = 10
b = 10
print(a==b) #comparison operato r
###########
a = 20
b = 10
print(a != b) 
##########

######################### Operator Precedence ###################

print(3*3+3/3-3) 

''' 
Rule for mathematical operations
PEMDAS
P: paranthesis
E: exponential 
M: multiplication
D: division
A: addition 
S: subtraction     

'''


# Identity Operator 
print(a is b)
print(a is not b)
