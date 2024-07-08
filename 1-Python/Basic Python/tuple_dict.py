#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:31:49 2024

@author: Sachin Borade
"""

####################### TUPLE in python ##########################


tup = ("cherry","cherry","banana")
print(tup)
print(tup[2]) # we can access the elements of tuple using indexing 

## NOTE:- Once the tuple is created, you cannot the change the entity 
#           or the values of tuple

x = ("apple","baanan","cherry")
x[1] = "kiwi" ## error

# To do the changed in tuple 
# 1) create tuple
# 2) change tuple to list
# 3) do the changes in list 
# 4) change list to tuple 

y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

## we can have different datatypes also 
x = ("apple",2,"banana")
print(x) # valid in tuple



## To join two or more tuple 
tuple1 = ("a","b","c")
tuple2 = (1,2,3)
tup = tuple1 + tuple2
print(tup)


################## DICTONARY in Python ##########################

dict1 = {"brand":"maruti",
         "model":"32323",
         "year":2023}
print(dict1) # Printing dictonary
print(len(dict1)) #length of dict
# it will only going to calculate the keys as length 
print(type(dict1))

## Creating the multivalue dictonary 
dict1 = {
            "brand" : ["maruti","mahendra","toyoto"],
            "model" : ["a","b","c"],
            "year" : [2011,2013,2023]
        }
print(dict1)

## get()
# it has key as a parameter to find the values of the key 

dict1.get("model")

## keys()
# Gives all the keys of dictonary 

dict1.keys()

################################################################

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:31:06 2024

@author: Sachin Borade
"""

car = {
         "brand":"ford",
         "model":"mustang",
         "year":1964
       }
x = car.keys()
print(x) #Printing keys
car["color"] = "white"
car
x = car.keys()
print(x) # Now you can see new keys has been added 
print(car)
#######

## pop() 
# To remove element from dictonary
car = {
         "brand":"ford",
         "model":"mustang",
         "year":1964
       }
car.pop("model") #It takes the --> key <-- as the argument
print(car)

### NOTE:- In list pop() method takes position as the argument.


#################
## Accessing keys in the dictonary 

for x in car:
    print(x)
    # It will print the keys in the dictonary 
    
for x in car:
    print(car[x])
    # It will print the items in the dictonary 

## If you want to access both keys and values 
for key, value in car.items():
    print("%s -> %s" % (key, value))


## Copying the Dictonary 
car = {
       "brand":"ford",
       "model":"mustang",
       "year":1964
       }

car1 = car # it will not make the copy of dictonary 
            # it will point towards the 
            # --> car <-- variable of dictonary 
# when there is changes in --> car <-- there is also changes on
# --> car1 <-- 




car = {
       "brand":"ford",
       "model":"mustang",
       "year":1964
       }
car2 = car.copy() #It will make the copy of that dictonary 
car2


car = {
       "brand":"ford",
       "model":"mustang",
       "year":1964
       }
dict1 = dict(car)
print(dict1)


## Nested Dictionaries
# A dictonary can contain dictionaries, 
# this is called nested dictionaries

our_family = {
                "child1":{
                            "name":"ram",
                            "dob":"21/5/2003"
                         },
                "child2":{
                             "name":"rohit",
                             "dob":"23/5/2003"
                         }
            }
print(our_family)
# We can have dictionary inside the dictionary 


## clear() method
# removes all the element from the dictonary 

car = {
       "brand":"ford",
       "model":"mustang",
       "year":1964
       }
car.clear() # It will return us the empty dictionary 
print(car)

## fromkey()
# Create a dictionary with 3 keys,all with one value

x = {'key1','key2','key3'}
y =0
thisdict = dict.fromkeys(x,y)
print(thisdict)

## get() 
# to get the value of dictionary 
car = {
       "brand":"ford",
       "model":"mustang",
       "year":1964
       }
car.get("model")

## items() 
# return the dictonary's key and value 

car.items() # dict_items([('brand', 'ford'), 
            # ('model', 'mustang'), ('year', 1964)])
# Instead of loop we can use above method also 
print(type(car.items())) # <class 'dict_items'>

## value() 
# display all the values of the dictionary 

car = {
       "brand":"ford",
       "model":"mustang",
       "year":1964
       }
car.values()


## update() 
# insert the items in the dictionary
car = {
       "brand":"ford",
       "model":"mustang",
       "year":1964
       }
car.update({"color":"white"})
print(car) # New item will be appended at the last

## replace() 


