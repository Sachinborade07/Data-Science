    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 09:23:47 2024

@author: Sachin Borade
"""
## break()
# Use break statement in loops 
fruits = ["apple","banana","orange"]
for i in fruits:
    print(i)
    if(i == "banana"):
        break

########################################

fruits = ["apple","banana","orange"]
for i in fruits:
    if(i == "banana"):
        break
    print(i)

## continue()
# it will not teminate the loop having true condition 
# ans else it will execute all the iteration in loops 

fruits = ["apple","banana","orange"]
for i in fruits:
    if(i == "banana"):
        continue
    print(i)
 
    
## range() function
# The range() function defaults to increment by 1, however 
# it is possible to specify the value by a third prameter
# range(start,end,step_up or step_down)
for i in range(1,10):
    print(i,end=" ") # 1 2 3 4 5 6 7 8 9
for i in range(1,10,2):
    print(i,end=" ") # 1 3 5 7 9 

## Nested loop 
# The loop inside the loop called nested loop's 

colors = ["green","yellow","red"]
fruits = ["guava","banana","apple"]
for x in colors:
    for y in fruits:
        print(x,y)




############### Function in PYTHON #################

###################### TYPE 1 ######################

# This is function without argument
def my_function():
    print("Hello from a function ")

my_function()

##################### TYPE 2 #######################

# This is function with argument k
def my_function(name):
    print("Hello "+name)
my_function("ram")


##################### TYPE 3 #######################

# This is function with positional argument
def my_function(name1,name2):
    print("hello "+name1+ " and "+ name2 )
my_function("ram", "sham")


##################### TYPE 4 #######################

# Arbitary argument *args
# If you dont know how many arguments that will be passed 
# into your function add a *before the parameter name the 
# defination 
def my_function(*kids):
    print(kids[0]+" "+kids[2])
my_function("Hello","World","India")


##################### TYPE 5 #######################

''' 
A keyword argument is where provide a name to the variable
as you pass it into the function .
One can think of the kwargs as being a dictionary that maps
each keyword to the value that we pass alongside it. 
That is why when we iterate over the kwargs there doesn't
seem to be any order in which they were printed out. 


'''

def myFun(**kwargs):
    for key,value in kwargs.items():
        print("%s == %s" % (key,value))
myFun(first="papalala",mid="mohanlal",last="goyal")

####################### TYPE 6  #######################

# The following example shows how to use a default parameter
# If we call the function without argument
# It uses the default value:
def my_function(country = "India"):
    print("I am from " + country )
    
my_function("Norway") #Norway #If I give parameter 
my_function() #India #If I don't give parameter

####################### TYPE 7  #######################

# passing the list as an argument 
fruits = ["apple","banana","guava"]
def my_function(fruits):
    for x in fruits:
        print(x)
my_function(fruits)


####################### TYPE 8  #######################

# Return value
# To let a function return a value 

def my_fun(x):
    return x*5
my_fun(5)

####################### TYPE 9  #######################

def my_fun():
    # SyntaxError: incomplete input
    
# here it will give us error 

## Pass function
def my_fun():
    pass
my_fun()
# having an empty function definition 
# like this would raise an error 
# without the passing any  argumen t

####################### TYPE 10  #######################

## Recurssive function 
# Find the factorial of number using recurssion 

def factorial(x):
    if x == 1:
        return 1
    else:
        return(x*factorial(x-1))
factorial(3) #6
factorial(6) #720

####################### TYPE 11  #######################

## Lambda function
# it also knows as anonymous function 
# a lambda function can take n number of arguments
# but can only have one expression

# 1) function declaration 
def add(a):
    sum = a+10
    return sum
# 2) function calling 
add(20)

# lambda function 
add = lambda a:a+10
print(add(20))

## lambda function can take any number of arguments
add = lambda a,b:a+b
print(add(5,6))

############################

## Finding odd numbers from the list 
lst = [34,12,64,55,75,13,63]
odd_lst = list(filter(lambda x:(x % 2 != 0),lst))
print(odd_lst)

# filter() method accepts two arguments in Python
# a function and an iterable such as a list 

# The function is called for every item in the list 

## Finding even numbers from the list 
lst = [34,12,64,55,75,13,63]
even_lst = list(filter(lambda x:(x % 2 == 0),lst))
print(even_lst)


## Finding square numbers from the list 

lst = [34,12,64,55,75,13,63]
sqr_lst = list(map(lambda x:(x*x),lst)) #here we are using map()
print(sqr_lst)
# when you want to apply a single transformation function 
# to all the iterable elements.



''' Write a python program using logical operator and if elif 
so  as to check height as welll as to charge the ticket price 
accordingly
'''


def pop_corn(x):
    return 400 * x

print("Welcome to the roller coaster")
height = int(input("Enter teh height in CM:-"))
if height >= 120:
    print("You are elligible for roller coaster")
    age = int(input("Enter your age in years:-"))
    bill = 0
    if age < 10:
        print("Child ticket is 500 $ ")
        bill = 500
    elif age >=10 and age<=15:
        print("the ticket charges is 1000$")
        bill = 1000
    elif age > 15 and  age < 25:
        print("the ticket charges is 1500$")
        bill = 1500
    elif age >= 25 and age <= 55:
        print("the ticket charges is 2000$ ")
        bill = 2000
    elif age > 55:
        print("the ticket price is 1400$")
        bill = 1400
    else:
        print("you are not elligible ")
        exit()
    popcorn = int(input("Enter the packet of pop corn:-"))
    x = pop_corn(popcorn)
    print("Your total bill is :-",bill + x,"$")
else:
    print("you are not elligible")

print("Hello")
x  =10



''' Case 2 '''

height = float(input("Enter the height in m:-"))
weight = float(input("Enter the weight in kg:"))
BMI = round((weight / (height*height)) ,2)
#or  BMI = round((weight / (height**2)) ,2)
if BMI < 18.5:
    print(f"You are underweight and you BMI is {BMI}")
elif BMI > 18.5 and BMI<25:
    print(f"You are normal and you BMI is {BMI}")
elif BMI >25 and BMI <30:
    print(f"You are overweight and your BMI is {BMI}")
elif BMI > 30 and BMI < 35:
    print(f"You are obese and your BMI is {BMI}")
elif BMI > 35:
    print(f"You are clinically obese and your BMI is {BMI}")
else:
    print(f"You need tretment immediately ")
##  You are normal and you BMI is 19.03


''' Case 3 
    find duplicate in the list
'''

lst1 = [1,2,3,1,3,1,2,2,3,2,1]
lst2 = [1,2,3]
def is_duplicate(lst1):
    for i in range(len(lst1)-1):
        for j in range(i+1,len(lst1)-1):
            if lst1[i] == lst1[j]:
                return True
    return False
is_duplicate(lst1)
is_duplicate(lst2)




''' 
Find the year is leap-year or not 
'''

## function definition
def is_leap(year):
    if( (year > 0) and (year % 4 == 0)  and (year % 100 == 0) or (year % 400 == 0)):
        return True
    return False

## function call
is_leap(2014)
is_leap(2024)




'''
    Mario Pyramid 
    Q) write a code to print the mario pyramid?
'''

for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print()

# mario pyramid
for i in range(4):
    for j in range(i+1):
        print("#",end=" ")
    print()
''' 
# 
# # 
# # # 
# # # # 
'''

# reverse mario pyramid
for i in range(4):
    for j in range(4-i):
        print("#",end=" ")
    print()
''' 
# # # # 
# # # 
# # 
# 
'''


# Diamond pattern printing 






#######################################################################

# Finding minimum and maximum 
lst = [23,45,2,1,3,4,34,54,34]
def min_max(lst):
    max_val = 0
    min_val = 1000
    for i in range(len(lst)-1):
        if(lst[i] > max_val):
            max_val = lst[i]
    print("The max value is :-",max_val)
    for i in range(len(lst)-1):
        if(lst[i] < min_val):
            min_val = lst[i]
    print("The min value is :-",min_val)
min_max(lst)



''' 
    # Check for is Paliandrome 

'''

######################################################################


def is_paliandrome(str1):
    rever = str1[::-1]
    if(str1 == ""):
        print("You have not entered the string:-")
        exit()
    if(str1 == rever):
        print("The string is Paliandrome")
    else:
        print("The list is not Paliandrome")
is_paliandrome("madam")
is_paliandrome("sachin")
is_paliandrome("step on no pets")

######################################################################

users = ['admin ','employee','worker','manager','staff']

for i in users:
    if i == "admin":
        print("Hello Sir, Do you want to see the status of company today")
    elif i == "employee":
        print("Have a nice day")
    elif i == "worker":
        print("Hello worker")
    elif i == "manager":
        print("Do you checked the list today")
    else:
        print("work hard, dream big")
        
        
        
        
 # Take the role input from the user      
role = input("Enter your role ")


def role_of_user(i):
    if i == "admin":
        print("Hello Sir, Do you want to see the status of company today")
    elif i == "employee":
        print("Have a nice day")
    elif i == "worker":
        print("Hello worker")
    elif i == "manager":
        print("Do you checked the list today")
    else:
        print("work hard, dream big")

role_of_user(role)
#######################################################################



## Design password using python 

#pick up the adjectives
adjectives = ['sleepy','slow','smelly','wet',
              'fat','red','orange','yellow','green',
              'blue','purple','fluffy','white',
              'proud','brave']

#pick up the nouns
noun = ['apple','dinosoour','ball','cat','toaster',
        'goat','dragon','panda','duck','mouse']

#pick up the words
import random
import string


# Function definition for pasword generator 
def password_generator(adjectives,noun):
    adjectives = random.choice(adjectives)
    noun = random.choice(noun)
    #Selecting a number
    number = random.randrange(0,100)
    
    #Selcting a special character
    special_char = random.choice(string.punctuation)
    
    password = adjectives + noun + special_char + str(number)
    print("Your Password is %s"%password)
password_generator(adjectives, noun) #Function calling for password generator


# You can use while if user is not satisfied with the password
print("Welcome to the password picker! ")
while True:
    password_generator(adjectives, noun)
    response = input("Would you like to generate another password (y/n): ")
    if response == "n":
        break



#making the noun upper in the code

# Function definition for pasword generator 
def password_generator(adjectives,nou):
    adjectives = random.choice(adjectives)
    nou = random.choice(noun)
    #Selecting a number
    number = random.randrange(0,100)
    
    #Selcting a special character
    special_char = random.choice(string.punctuation)
    
    password = adjectives + nou.upper() + special_char + str(number)
    print("Your Password is %s"%password)

password_generator(adjectives, noun) #Function calling for password generator


































