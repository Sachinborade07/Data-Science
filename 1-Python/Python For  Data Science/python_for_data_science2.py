#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 08:42:12 2024

@author: Sachin Borade
"""

# NUMPY 
# It stands for numerical python
# which consist of multidimentional array

'''

list can store heterogeneous entity  and
numpy array can store homogeneous entity 

'''

import numpy as np
arr = np.array([10,20,30])
print(arr) # [10 20 30]
print(type)

# Create Multidimentional Array
arr = np.array([[10,20,30],[40,50,60]])
print(type(arr))
print(arr)
'''
[[10 20 30]
 [40 50 60]]
'''

# Represent the Minimum Dimension 
# use ndom param to specify how many minimum 
# dimension you wanted to create an array with # MINIMUM DIMENTION

arr = np.array([10,20,30,40],ndmin=3)
arr

## We can have complex datatype also 

arr = np.array([10,20,30,40],dtype=complex)
arr

# Get the dimension of array 
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr.ndim)

# Finding the size of each item in the array 
arr = np.array([10,20,30])
print("Each item contain in bytes :",arr.itemsize)

# Get the shape and size of Array 
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("Array Size:-",arr.size)
print("Array Shape:-",arr.shape)

# Creating array form list with type float 
arr = np.array([[1,2,3],[4,5,6]],dtype=float)
print(arr)


###############################################################################

#Create a sequence of integers using a arange()

arr = np.arange(0,20,2)
arr


## 
arr = np.arange(11)
arr

## Accessing single element using index 
arr[2]
arr[-5]


## Multi-dimentional array indexing
arr = np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(arr)

print(arr.shape)
# (2,5)

print(arr[1,1])
#     -5-4-3-2-1
#      0 1 2 3 4
# 0  [[1 2 3 4 5]
# 1  [6 7 8 9 0]]


print(arr[1][-1])


###############

## Accessing array elements using slicing 
arr = np.array([0,1,2,3,4,5,6,7,8,9])
x = arr[1:8:2] # [1 3 5 7]
print(x)
x = arr[-2:3:-1] # [8 7 6 5 4]
print(x)



import numpy as np
## Slicing multi-dimentional array 
mul_arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [34,3,2,4],
                [4,5,3,4]
               ])

# For multi-dimentional NumPy arrays 
# you can access the elements as below 

mul_arr[1,2] # 7
mul_arr[1,:] #  array([5, 6, 7, 8])
#Accessing values at rows 

mul_arr[:,1] # array([2, 6, 3, 5])
#Accessing values at columns

x = mul_arr[:,::2]
print(x)

x = mul_arr[1:3,1:3]
print(x)


x = 3 # Scaler
x = [10 20 30] #vectors
x = [[10,20,30],[40,50,60]] #Matrix 
x = [[[10,20,30]]] #Tensors



# Integer array Indexing 
arr = np.arange(12).reshape(3,4)
print(arr)


# Boolean array Indexing 
import numpy as np
arr = np.arange(12).reshape(3,4)
arr
# Boolean array Indexing 
rows = np.array([False,True,True])
rows
wanted_rows = arr[rows,:]
# It will select the rows based on the boolean array
# as 0th row will not be selected and 1 and 2 row will get selected
print(wanted_rows)


# Converting List() to Numpy array by numpy.asarray() method
list = [20,30,40,50]
array = np.asarray(list)
print("Array:- ",array)
print(type(array))

# Numpy array properties

    #ndarray.shape
    #ndarray.ndim
    #ndarray.itemsize
    #ndarray.size
    #ndarray.dtype


# ndarray.shape 
array = np.array([[1,2,3],[4,5,6]])
array
print(array.shape)

# ndarray.ndim
print(array.ndim)

# ndarray.itemsize
print(array.itemsize)

# ndarray.size
print(array.size)

# ndarray.dtype
print(array.dtype)


array = np.array([[1,2,3],[4,5,6]])
new_array1 = array.reshape(3,2)
print(new_array1)
new_array2 = array.shape = (3,2)
print(new_array2)


###############################################################################

# Arithmetic operation on array 
arr1 = np.arange(16).reshape(4, 4)
arr1
arr2 = np.array([1,3,2,4])
arr2


# add() function 
add_arr = np.add(arr1,arr2)
print(f"Adding two arrays: \n {add_arr}")
'''
         [[ 0,  1,  2,  3],                           [[ 1  4  4  7]
         [ 4,  5,  6,  7],       [1, 3, 2, 4]         [ 5  8  8 11]
         [ 8,  9, 10, 11],                            [ 9 12 12 15]
         [12, 13, 14, 15]]                            [13 16 16 19]]
                                    
'''

# subtract() function 
sub_arr = np.subtract(arr1,arr2)
print(f"Subtraction of two arrays: \n {sub_arr}")
'''
[[-1 -2  0 -1]
[ 3  2  4  3]
[ 7  6  8  7]
[11 10 12 11]]
'''

# multiply() function
mul_arr = np.multiply(arr1,arr2)
print(f"Multiplication of two arrays: \n {mul_arr}")
'''
 [[ 0  3  4 12]
 [ 4 15 12 28]
 [ 8 27 20 44]
 [12 39 28 60]]
'''

# divide() function 
div_arr = np.divide(arr1,arr2)
print(f'Division of two array:\n {div_arr}')
'''
[[ 0.           0.33333333       1.          0.75  ]
[  4.           1.66666667       3.          1.75  ]
[  8.           3.               5.          2.75  ]
[  12.          4.33333333       7.          3.75  ]]
'''


# to perform Reciprocal operation 
arr1 = np.array([50,10.3,5,1,200])
rep_arr = np.reciprocal(arr1)
print(f"After applying reciprocal function to array: \n {rep_arr}")
'''
 [0.02       0.09708738 0.2        1.         0.005     ]
'''

# power() function 
arr1 = np.array([1,2,3,4,5])
power = np.power(arr1,2)
print(f"After application of power array:-\n {power}")
'''  [ 1  4  9 16 25] '''



# We can have the power of one array to other array 
# The every index of array1 is get power of every index of array2 
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([5,4,3,2,1])
print("My second array: \n ",arr2)
pow_arr = np.power(arr1,arr2)
print(f"After applying power function to array:\n {pow_arr}")


# mod() function 
# this function return us the remainder

import numpy as np
arr1 = np.array([7,20,13])
arr2 = np.array([3,5,2])
arr1
arr2

# mod()
mod_arr = np.mod(arr1,arr2)
print(f"After applying mod function to array: \n {mod_arr}")
'''[1 0 1] our output as --> 7 % 3 = 1 --> 20 % 5 = 0 --> 13 % 2 = 1'''


