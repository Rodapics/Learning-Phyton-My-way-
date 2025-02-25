# -*- coding: utf-8 -*-
"""SimuladoresCuanticos_Taller3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fg8-8hsoloe6hmnkPVXW_i9_EVvFfFwy
"""

import numpy as np
import matplotlib.pyplot as plt
import cmath

I = np.identity(4) # Identity matrix
O_matrix = np.zeros((4, 4)) # Cero matrix
o_vector = np.zeros((1, 4)) # Cero vector
v = np.array([1, 0, 0, 0]) # Unitary vector v
u = np.transpose(v) # Transpose of v

# Definition of state matrix
A = np.array([
    [u, I, I, v],
    [u, I, I, o_vector],
    [u, O_matrix, I, o_vector]
])

# Coefficient calculations

C2000= np.dot(np.dot(np.dot(A[2,0], A[0,1]), A[0,2]), A[0,3])
C1100= np.dot(np.dot(np.dot(A[1,0], A[1,1]), A[0,2]), A[0,3])
C0020= np.dot(np.dot(np.dot(A[0,0], A[0,1]), A[2,2]), A[0,3])
C1110= np.dot(np.dot(np.dot(A[1,0], A[1,1]), A[1,2]), A[0,3])

print("The coefficients C2000, C1100, C0020, C1110 are, respectively: " + str(C2000) + ", " + str(C1100) + ", " + str(C0020) + ", " + str(C1110))

# The norm is given by the square root of the square coefficient sum:

Norm = np.sqrt(C2000**2+C1100**2+C0020**2+C1110**2)
print("The norm of the state is " + str(Norm))

# Normalizing the state:
v = (1/np.sqrt(Norm))*v
u = np.transpose(v)

# Definition of new state matrix
A = np.array([
    [u, I, I, v],
    [u, I, I, o_vector],
    [u, O_matrix, I, o_vector]
])

# Coefficient calculations

C2000= np.dot(np.dot(np.dot(A[2,0], A[0,1]), A[0,2]), A[0,3])
C1100= np.dot(np.dot(np.dot(A[1,0], A[1,1]), A[0,2]), A[0,3])
C0020= np.dot(np.dot(np.dot(A[0,0], A[0,1]), A[2,2]), A[0,3])
C1110= np.dot(np.dot(np.dot(A[1,0], A[1,1]), A[1,2]), A[0,3])

Norm = np.sqrt(C2000**2+C1100**2+C0020**2+C1110**2)

print("The new coefficients C2000, C1100, C0020, C1110 are, respectively: " + str(C2000) + ", " + str(C1100) + ", " + str(C0020) + ", " + str(C1110) + " and the new norm is " + str(Norm))