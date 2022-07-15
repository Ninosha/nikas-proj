# import numpy as np
#
# #
# # # Defining 1D array
# # my1DArray = np.array([1, 8, 27, 64])
# #
# # print(my1DArray)
# # print("-------------------------------")
# # # Defining and printing 2D array
# # my2DArray = np.array([[1, 2, 3, 4], [2, 4, 9, 16], [4, 8, 18, 32]])
# # print(my2DArray)
# # print("-------------------------------")
# #
# # #Defining and printing 3D array
# #
# # my3Darray = np.array([[[ 1, 2 , 3 , 4],[ 5 , 6 , 7 ,8]], [[ 1, 2, 3, 4],[ 9, 10, 11, 12]]])
# # print(my3Darray)
# #
# # print("-------------------------------")
# #
# # #Defining and printing 3D array
# #
# # my4Darray =[[[ 1, 2 , 3 , 4],[ 5 , 6 , 7 ,8]], [[ 1, 2, 3, 4],[ 9, 10, 11, 12]]]
# # print(my4Darray)
# #
# #
# # # Print out memory address
# # print(my2DArray.data)
# # # Print the shape of array
# # print(my2DArray.shape)
# # # Print out the data type of the array
# # print(my2DArray.dtype)
# # # Print the stride of the ar
# # # Array of ones
# # ones = np.ones((3,4))
# # print(ones)
# # # Array of zeros
# # zeros = np.zeros((2,3,4),dtype=np.int16)
# # print(zeros)
# # # Array with random values
# # np.random.random((2,2))
# # # Empty array
# # emptyArray = np.empty((3,2))
# # print(emptyArray)
# # # Full array
# # fullArray = np.full((2,2),7)
# # print(fullArray)
# # # Array of evenly-spaced values
# # evenSpacedArray = np.arange(10,25,5)
# # print(evenSpacedArray)
# # # Array of evenly-spaced values
# # evenSpacedArray2 = np.linspace(0,2,9)
# # print(evenSpacedArray2)
# #
# #
# # # Print the total consumed bytes by `my2DArray`'s elements
# # print(my2DArray.nbytes)
#
#
# # Rule 1: Two dimensions are operatable if they are equal
# # Create an array of two dimension
# A = np.ones((6, 8))
# # Shape of A
# print(A.shape)
# # Create another array
# B = np.random.random((6, 8))
# # Shape of B
# print(B.shape)
#
# # Sum of A and B, here the shape of both the matrix is same.
# print(A)
# print(B)
# print(A + B)

import numpy as np

#
# x = np.array([10, 20, 30, 40, 50])
# # Select items at index 0 and 1
#
# # Select item at row 0 and 1 and column 1 from 2D array
# y = np.array([
#     [1, 2, 3, 4],
#     [9, 10, 11, 12],
#     [9, 122, 131, 12]
#
# ])
# print(y)
# print(y[0:3, 1:3])
# # Specifying conditions
# biggerThan2 = (y >= 2)
# print(y[biggerThan2])
