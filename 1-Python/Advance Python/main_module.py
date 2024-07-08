#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:54:29 2024

@author: sachin
"""
# Here we are calling the time_it decorator from wrapper.py file
from wrapper import time_it

@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result



array = range(1,10000)
time_square = calc_square(array)
time_cube = calc_cube(array)
