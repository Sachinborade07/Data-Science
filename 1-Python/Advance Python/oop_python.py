#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:01:51 2024

@author: Sachin Borade
"""

class Human:
    # Constructor doesn't return the value
    def __init__(self,n,o):
        self.name = n
        self.occupation = o
    
    #Creating the methods for the object
    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, "Plays tennis")
        elif self.occupation == "actor":
            print(self.name, "shoots film")
    
    def speaks(self):
        print(self.name, "says how are you ? ")



# creating the object
tom = Human("Tom cruise","actor")
tom.do_work()
tom.speaks()

# creating another object 
maria = Human("Maria Sharapova","Plays tennis")
maria.do_work()
maria.speaks()


############################################################################


### Inheritance in OOP

class vehicle:
    def general_usage(self):
        print("General work: Transportation by")


class Car(vehicle):
    def __init__(self):
        print("I am car")
        self.wheels = 4
        self.has_roof = True
    
    def specific_usage(self):
        self.general_usage()
        print("Specifically Used for 4 - 7 peoples")
        
class motercycle(vehicle):
    def __init__(self):
        print("I am Motercycle")
        self.wheels = 2
        self.has_roof = False
        
    def specific_usage(self):
        self.general_usage()
        print("Specifically Used for 2 peoples")
        
c = Car()
c.specific_usage()
m = motercycle()
m.specific_usage()


############################################################################


### Multiple Inheritance in OOP
# child class having more than one base class called as Multiple Inheritance.


class Father():
    def skills(self):
        print("I like gardening & programming")

class Mother():
    def skills(self):
        print("I like cokking & art")

class child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("I like sports")
        
c = child() ## Object for child class is created 
c.skills() ## accessing the two base classes using object of child class.

        
        
            



