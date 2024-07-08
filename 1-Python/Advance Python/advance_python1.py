
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:30:22 2024

@author: Sachin Borade
"""

## Adding element in list using loop

lst = []
for num in range(0,20):
    lst.append(num)
print(lst)

## List Comprehesion

lst = [num for num in range(0,20)]
print(lst)


names = ['dada','mama','kaka']
lst = [name.capitalize() for name in names] # It will capitalize the 
print(lst)                                  # First name of words


## List comprehension with if statement 
def is_even(num):
    return num % 2 == 0
lst = [num for num in range(10) if is_even(num)]
print(lst)
# We need to use conditional statement after the for loop 


## List comprehension with nested for loops
lst = [f"{x}{y}" for x in range(3) for y in range(3)]
print(lst)
# We need to write business logic on left hand side and both the for 
# loops on right hand side

### Dictonary Comprehension
dict = {x:x*x for x in range(3)}
print(dict)
# Here our business logic is at left hand side and for loop at right side

#################################################################

#Generator 
# It is another way of creating iterators 
# In a simple way where 
# It used the keyword "yield"
# Instead of returning it in a defined function
# Generators are implemented using a function

gen = (x for x in range(3))
print(gen)
print(type(gen))
for num in gen:
    print(num)

# It is going to hold the values 
gen = (x for x in range(3))
gen
next(gen)
next(gen)
next(gen)
next(gen) # After getting the generator empty we get
          # StopIteration error
print(type(gen)) #It has the type as " <class 'generator'> "

###################################################################
# Function which return multiple values

def range_even(end):
    for num in range(0,end,2):
        return num
for num in range_even(6):
    print(num)
   # It is not possible for "return" to return us multiple value 
   # that's why we are using "yield" function
   
#####################

def range_even(end):
    for num in range(0,end,2):
        yield num
        
# Accessing using for loop
for num in range_even(6):
    print(num)

# Instead of using for loop we can write our own generator function
gen = range_even(6)
next(gen)
next(gen)


# Chaining Generators
def lengths(itr):
    for ele in itr:
        yield len(ele)
'''  This function takes an iterable itr as input and yields the length of 
 each element in the iterable. '''
def hide(itr):
    for ele in itr:
        yield ele*'*'
        
'''This function takes an iterable itr as input and yields each 
   element of the iterable, but replaces each character in the element 
   with an asterisk (*). '''
''' 

    'ele* ' appears to be a placeholder for an element from an iteratble.
    The asterik(*) is likely just a character used to represent a placeholder
    or a wildcard.
    For an instance, if you're iterating over a list of elements, "ele*"
    could symbolize any element in that list.
    It's a generic representation that doesn't correspond to any specific 
    syntax in Python or itertools. 
    
'''



password = ['welcome@1','helloworld',"I-LoveYou"]

for passw in hide(lengths(password)):
    print(passw)
# Here we can see our password is get hided



###################### Problem Definition #######################

# Take the password input from user and hide the password

passwords=""
def password_generator():
    noun = input("Enter the noun for the password:-")
    adjective = input("Enter the adjective for the password:-")
    print("Randomly picking up the number")
    # Selecting number
    import random
    number = random.randrange(0,9)
    
    passwords = adjective + noun + str(number)
    print("Your Password is :- ",passwords)
    
    # Now lets hide the password
    def lengths(itr):
        for ele in itr:
            yield len(ele)
    def hide(itr):
        for ele in itr:
            yield ele*'*'
    # Hiding password 
    hidden = hide(lengths(passwords))
    print(hidden)

password_generator()


#################### above there is some error ############################

## Enumerate 
# Printing the list with index 

lst = ["milk","egg","bread"]
for index in range(len(lst)):
    print(f"{index + 1} {lst[index]}")

## same code can be implemented using enumerate 
lst = ["milk","egg","bread"]
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")
# It allows us to keep track of the number of iterations in a loop

##########################################################################

## Use of zip function 

name = ["data","mama","kaka"]
info = [9898,39483,493849]
for nm,inf in zip(name,info):
    print(nm,inf)
    
''' 
    Combine multiple lists into a single list of tuples, Iterate over 
    multiple iterables in parallel 
''' 


## Use zip function with mis-match list 
name = ["data","mamaf","kaka","kaki"]
info = [9898,39483,493849]
for nm,inf in zip(name,info):
    print(nm,inf)
# It will not display the excess mis-match item in name list
# i.e. kaki

## for that we use zip_longest

from itertools import zip_longest 
name = ["data","mama","kaka","kaki"]
info = [9898,39483,493849]
for nm,inf in zip_longest(name,info):
    print(nm,inf)
# It will print infront of (kaki == None)

## Use the fillvalue instead of getting None 
name = ["data","mama","kaka","kaki"]
info = [9898,39483,493849]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)
# Here you can observe that the instead of None -> 0 is filled.



### Use of all()
''' 
    returns TRUE if all of the items of a provided iterable 
    (List, Dictionary, Tuple, Set, etc.) are non-zero; otherwise, 
    it returns FALSE.
    
'''

lst = [2,3,-6,8,9] #value must be non-zero
if(all(lst)):
    print("There are no null values")
else:
    print("There are null values")

lst = [2,0,-6,8,9] #value must be zero
if(all(lst)):
    print("There are no null values")
else:
    print("There are null values")



### Use of any()

'''
    returns TRUE if any of the items of a provided iterable
    (List, Dictionary, Tuple, Set, etc.) are non-zero ; otherwise, 
    it returns FALSE.  
    
'''

lst = [0,0,0,2,0]
if any(lst):
    print("It has some value non-zero value")
else:
    print("All the values are zero in the list")


## count() function
## importing count
from itertools import count
counter = count()
print(next(counter))
print(next(counter))
print(next(counter))


#####  Start counter starting from -> 1

from itertools import count
counter = count(start = 1)
print(next(counter)) # here it will start counting from 1
print(next(counter))
print(next(counter))


''' The counter in Python is a function that is used to count the 
number of times an element appears in a list. '''

########
from collections import Counter

my_list = [1, 2, 3, 4, 5, 1, 2, 3]

# Create a counter object
counter = Counter(my_list)

# Print the counter object
print(counter)
0# Counter({1: 2, 2: 2, 3: 2, 4: 1, 5: 1})
# It will count the number of elements in the list 


## cycle() function

''' 
    The cycle() function can be useful for a variety of tasks, 
    such as creating infinite sequences, generating random samples, 
    and iterating over a list of elements multiple times. 
'''

import itertools
instructions = ("Eat","Code","Sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)


## repeat() function 
from itertools import repeat
for msg in repeat("keep patience",times=3):
    print(msg)

''' 
    The repeat() function in Python is used to repeat an object
    a specified number of times. It can be used to repeat strings, 
    lists, tuples, dictionaries, and other objects.
'''

########################## permutation and combination ####################



## combination function 
from itertools import combinations
players = ["rohit","sachin","virat"]
for i in combinations(players, 2):
    print(i)
# It will print all the combination as per the mathematics 
# or make the part of two players uniquely 


## Let's have the team of 5 players randomly selected
players = ["rohit","sachin","virat","gill","faf-duplesy","dhoni"]
for i in combinations(players, 5):
    print(i)


### permutation() function 

# Seating arrangment for people using permutation 

lst = ["ram","sham","ghansham"]
from itertools import permutations
for seat in permutations(lst,2):
    print(seat)


###########################################################################

## product() function 
from itertools import product
item_a = ['Rohit','Pandya','Bumrah']
item_b = ['Virat','Manish','Sami']
for pair in product(item_a,item_b):
    print(pair)
##################################



# filter() function
age = [27,17,18,34]
adults = filter(lambda age:age>=18,age)
print([age for age in adults])

########################################################################

''' 
    In python, assignmnet statements (obj_a = obj_b) 
    does not create real copies.
    It only created a new variable with same reference
    So when you want to make actual copies of mutable objects (list,dict)
    and want to modify the copy without affecting the original, you to 
    be careful.
    For 'real' copies we can use the copy module.
    However, for compund/ nested objects 
    
    There is important difference between shallow and deep copying 
    * Shallow copying:-Shallow copying creates a new object that
                        references the same inner objects as the original.
                        This means that if you change one of the inner 
                        objects in the shallow copy, it will also change 
                        in the original object.
   * Deep copying:- Deep copying creates a completely independent copy 
                   of both the object and its inner objects. 
                   This means that if you change one of the inner objects 
                   in the deep copy, it will not change in the original 
                   object.
'''
# This will only create a new varible with same reference


list_a = [1,2,3,4,5]
list_b = list_a 

list_a[0] = 0
print(list_a)
print(list_b)
print(id(list_a))
print(id(list_b))
## We can see both the things holding the same values. 
#  as well as they also have same id()

## This is Shallow Copying 
# One level1 deep:- Modifying on level-1 does not affect

import copy 
list_a = [1,2,3,4,5]
list_b = copy.copy(list_a)

list_b[0] = -10
print(list_a) # [1, 2, 3, 4, 5]
print(list_b) # [-10, 2, 3, 4, 5]
# Both the lists have different values


# Second level2 deep:- Trying to modify on level-2 
import copy
list_a = [[1,2,3,4,5],[6,7,8,9]]
list_b = copy.copy(list_a)
list_b[0][0] = 10
print(list_a) # [[10, 2, 3, 4, 5], [6, 7, 8, 9]]
print(list_b) # [[10, 2, 3, 4, 5], [6, 7, 8, 9]]
# Shallow copying will not work will nested lists
# It have changed the both the values 


##########################################################################

## This is Deep Copying 
#Fullindependent
import copy
list_a = [[1,2,3],[4,5,6]]
list_b = copy.deepcopy(list_a)
list_b[0][0] = -19
print(list_a) #[[1, 2, 3], [4, 5, 6]]
print(list_b) #[[-19, 2, 3], [4, 5, 6]]

# Deep copying will work with nested lists also 
# It will affect on only one list 


"""
Created on Tue Mar 26 09:18:25 2024

@author: Sachin Borade
"""
import pandas as pd
f1 = pd.read_csv("/home/sachin/Desktop/Data Science/1-Python/csv_files/buzzers.csv")
# It is absolute path for the file 
print(type(f1))

############################################################################

#Check for working directory
import os 
with open("/home/sachin/Desktop/Data Science/1-Python/csv_files/buzzers.csv") as raw_data:
    print(raw_data.read())

############################################################################

# Reading CSV data in the form of list
import csv
with open("/home/sachin/Desktop/Data Science/1-Python/csv_files/buzzers.csv") as raw_data:
    for line in csv.reader(raw_data): # Here it is csv.reader() to read data
        print(line)

############################################################################

# Reading CSV data as dictionaries
import csv
with open("/home/sachin/Desktop/Data Science/1-Python/csv_files/buzzers.csv") as raw_data:
    for line in csv.DictReader(raw_data): #Here it is csv.DictReader to read data 
        print(line)

############################################################################


##   Go through the documentation for the (csv module) 



############################################################################

with open("/home/sachin/Desktop/Data Science/1-Python/csv_files/buzzers.csv") as data:
    flights = {}
    for line in data:
        if ',' in line:  # Check if the line contains a comma
            k, v = line.split(",", 1)  
            # Split only once to prevent multiple splits 
            #if there are commas in the value
            flights[k] = v  
            # Remove any leading/trailing whitespace
print(flights)


############################################################################

# pre-requisite to decorators 
def plus_one(number):
    number1 = number + 1
    return number1
plus_one(5)

## Function inside the other functions
def plus_one(number):
    
    def add_one(number):
        number1 = number + 1 
        return number1
    
    result = add_one(number)
    return result
plus_one(5)

############################################################################

## Passing the function as a argument to other function
def plus_one(number):
    result1 = number + 1
    return result1

def function_call(function):
    result = function(5)
    return result

function_call(plus_one)

############################################################################

## Function Returning other Functions
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
hello()


#### try all these things on https://pythontutor.com/render.html#mode=display
### The above link is very good for visualization 


## Need for decorators

## calculating time for square
import time
def calc_square(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number * number)
    end = time.time()
    total_time = (end - start) * 1000 # When we want result in miliseconds
    print(f"Total time for execution square is {total_time}")
    return result


## calculating time for cube
def calc_cube(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number * number * number)
    end = time.time()
    total_time = (end - start) * 1000 # When we want result in miliseconds
    print(f"Total time for execution cube is {total_time}")
    return result

array = range(1,10000)
time_square = calc_square(array)
time_cube = calc_cube(array)

############################################################################

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 08:30:18 2024

@author: Sachin Borade

"""

# A python decorator is a function 
# that takes function as a argument and return it by adding 
# some functionality

def say_hi():
    return 'hello there'

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
decorate = uppercase_decorator(say_hi)
decorate()



def say_hi():
    return 'hello there'

def uppercase_decorator(function):
    def wrapper():
        return function().upper()
    return wrapper
decorate = uppercase_decorator(say_hi)
decorate()


############################################################################

# For us to apply decorators. 
# We simply use @ symbol before
# the function we would like to decorate()

def uppercase_decorator(function):
    def wrapper():
        return function().upper()
    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'
say_hi()

############################################################################

# Applying multiple Decorators to single function 
# We can use multiple decorators to a single function. However,
# the decorators will be applied in the order that we've called them. 

def split_string(function):
    def wrapper():
        return function().split()
    return wrapper
def uppercase_decorator(function):
    def wrapper():
        return function().upper()
    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'
say_hi()



############################################################################

#Calculating the time using decorators
#1) for square 2) for cube
import time 
def time_it(function):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = function(*args,**kwargs)
        end = time.time()
        total_time = (end - start) * 1000
        print(function.__name__ + f"taken {total_time} mil sec")
        return result
    return wrapper

# calling decorator for square function
@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

# calling decorator for cube function
@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,10000)
time_square = calc_square(array)
time_cube = calc_cube(array)


##########################################################################
