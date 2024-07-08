#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:50:51 2024

@author: Sachin Borade
"""
#####    LIST in python ##########

lst = ["cherry","banana","apple"]
print(lst)

## Accessing the list using positive indexing
print(lst[0])
## Accessing the list using negative indexing
print(lst[-1])

## Adding the element into the list
lst.append("mango") 
print(lst)

## Remove elements from the list 
lst.clear()
print(lst)


#### Copyting the list ########

lst = ["cherry","banana","apple"]
lst1 = lst
lst.append("mango")
print(lst)
print(lst1) # The changes will going to be occur in both list


## copy() 
# So we are going to use copy() method in python 
lst2 = lst.copy()
lst2.append("guava")
print(lst)
print(lst2)

## count()
#  It will return the integer value of occurring element

lst = ["cherry","banana","apple","cherry"]
lst.count("cherry")

## extend()
# Used to add the list into the list at the end 

lst1 = [1,2,3]
lst2 = [4,5,6]
lst1.extend(lst2)
print(lst1)

## insert() 
# to insert the element at specific location

lst = ["cherry","cherry","mango"]
lst.insert(0,"mango")
print(lst)


## pop()
# used to remove the element at specific location

lst = ["cherry","cherry","mango"]
lst.pop(2) #This is the location where we want remove the item 
            # The number is indexed number
            

## remove ()
# Will remove the cherry which is going to be occur at the first 

lst = ["cherry","cherry","mango"]
lst.remove("cherry")
print(lst)

## reverse()
# Will going to reverse the content of the list

lst = ["banana","cherry","mango"]
lst.reverse()
print(lst)

## sort()
# it will going to sort the entites of the list in alphabetical 
# order 
lst = ['mango', 'cherry', 'banana']
lst.sort() #it wil sort the list
print(lst)











