#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:53:11 2024

@author: sachin
"""

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
