#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:58:03 2024

@author: Sachin Borade
"""
import numpy as np 
print(np.__version__)
# 1.26.4

from numpy import empty 

a = empty([3,3])
print(a)

'''
[[3.3733481e-316 0.0000000e+000 0.0000000e+000]
 [0.0000000e+000 0.0000000e+000 0.0000000e+000]
 [0.0000000e+000 0.0000000e+000 0.0000000e+000]]
'''


## Create a zero array 
from numpy import zeros 
a = zeros([3,5])
print(a)

## Create a ones array 
from numpy import ones
a = ones([3])
print(a)

############################

## Create array with vstack
from numpy import array 
from numpy import vstack

# Create first array 
a1 = array([1,2,3])
print(a1)
# Crate second array 
a2 = array([4,5,6])
print(a2)

# Create Vertical Stack
a3 = vstack((a1,a2))
a3
# or 
a3 = vstack([a1,a2])
print(type(a3))
print(a3.shape)
# In both the cases we get the same type of output 

############################

## Create array with hstack
from numpy import array 
from numpy import hstack

# Create first array 
a1 = array([1,2,3])
print(a1)
# Crate second array 
a2 = array([4,5,6])
print(a2)

# Create Horizontal Stack
a3 = hstack((a1,a2))
a3
# or 
a3 = hstack([a1,a2])
print(type(a3))
print(a3.shape)
# In both the cases we get the same type of output 

############################

# Index array out of bounds
from numpy import array 
#define array 
data = array([[1,2,3,4],[5,6,6,7]])
print(data[1][3])

# index row of two-dimentional array 
from numpy import array 
# define array 
data = array ([
    [1,2],
    [3,4],
    [5,6]
    ])

# index data
print(data[0,])
# 0th row and column 

############################

# slice one dimentional array 
from numpy import array 
#define array
data = array([1,2,3,4,5])
print(data[1:3])

###########################
# negative slicing of one-dimentional array 
from numpy import array 
# define array 
data = array([1,2,3,4,5])
print(data[-2:])

############################
# Split input and output data
from numpy import array 
# define array 
data = array ([
    [1,2,3],
    [3,4,5],
    [5,6,7]
    ])
# Seperate data 
X,y = data[:,:-1],data[:,-1]
X
y


###########################################################################
# broadcast scalar to one-dimentional array 
from numpy import array 
#define array 
a = array([1,2,3])
print(a)
# define scalar 
b = 2
print(b)

#broadcast
c = a + b
print(c)

##################################
#Vector addition 
from numpy import array 
# define first vector 
a = array([1,2,3])
print(a)
# define second vector 
b = array([4,5,6])
print(b)

#Vector Addition 
c = a + b
print(c)


#############################################################################

# Vector L1 Norm

'''
THe L1 norm is calculated as the sum of absolute vectors values,
where the absolute value of a scalar uses the notation |a1|.
In effect, the norm is a calculated of the Manhattan distance from the 
origin of the vector space. 

'''

# it is calculated as 
# |V| = |a|+|b|+|c|

from numpy import array 
from numpy.linalg import norm 
# define vector 
a = array([1,2,3])
print(a)
#calculate norm
l1 = norm(a,1)
print(l1)

###############################################################################

# Vector L2 Norm
'''
To calculate the L2 Norm of a vector take the square root of the sum 
of the squared vector values. 
Another name for L2 norm of a vector is Euclidean Distance.
This is often used for calculation the error in machine learning models. 

'''

from numpy import array 
from numpy.linalg import norm
# define vector 
a = array([1,2,3])
print(a)
#calculate norm 
l2 = norm(a)
print(l2)


###############################################################################

# Triangular Matrices 
from numpy import array 
from numpy import tril
from numpy import triu 
# define square matrix
M = array([
    [1,2,3],
    [1,2,3],
    [1,2,3]
    ])
print(M)

# lower triangular matrix 
lower = tril(M)
print(lower)

# upper triangular matrix
upper = triu(M)
print(upper)

############################

# diagonal matrix
from numpy import array 
from numpy import diag
# define square matrix 
M = array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ])
print(M)

# Extract the diagonal matrix
d = diag(M)
print(d)

# Create diagonal matrix from vector
D = diag(d)
print(D)

############################
# Identity Matrix

from numpy import identity 
I = identity(3)
print(I)

############################
# Orthogonal Matrix 

'''
If the matrix is orthogonal then product of matirx and its transpose give 
us identity Matrix 
     ##   |A| * |A|^T == I
'''
from numpy import array 
from numpy.linalg import inv
# define orthogonal matrix 
Q = array([
            [1,0],
            [0,-1]
            ])
print(Q) 

# inverse equivalence
I = Q.dot(Q.T)
print(I)

############################

## Traspose of Matrix 
from numpy import array
A = array([
    [1,2],
    [3,4],
    [5,6]
    ])
print(A)
# Calculate Transpose
C = A.T
print(C)

############################

## Inverse of Matrix 
from numpy import array 
from numpy.linalg import inv
A = array([
    [1,2],
    [3,4]
    ])
print(A)
# Inverse Matrix 
B = inv(A)
print(B)

# Multiply A and B
I = A.dot(B)
print(I)

############################

## Sparse Matrix 
from numpy import array 
from scipy.sparse import csr_matrix
# Create Dense Matrix
A = array([
    [1,0,0,1,0,0],
    [0,0,2,0,0,1],
    [0,0,0,2,0,0]
    ])
print(A)

# Convert to sparse matrix (CSR method)
S = csr_matrix(A)
print(S)
# Reconstruct Dense matrix 
B = S.todense()
print(B)

############################

