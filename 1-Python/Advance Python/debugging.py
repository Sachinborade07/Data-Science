#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:24:37 2024

@author: sachin
"""

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