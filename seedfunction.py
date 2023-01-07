# various useful functions in numpy module 
# 1. zeros --- this funciton creates an array (either one dimen. or 2 dimen) and fill all the alues with zero (0).
import numpy as np
arr=np.zeros(5)
# example of one dimention array
print(arr)#[0. 0. 0. 0. 0.]
row,column=3,5
arr=np.zeros((row,column))
print(arr)
# [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]

# 2. ones -- same as zeros 
row,column=2,3
arr=np.ones((row,column))
print(arr)
arr=np.ones(10)
print(arr)
# [[1. 1. 1.]
#  [1. 1. 1.]]
# [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

# 3. eye(row,column) it will return a matrix whose diagonal matrix will filled with 1 and all other values with zero 0
import numpy as np
arr=np.eye(3)
#it will return a square matrix of 3 x 3 ... 
print(arr)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
arr = np.eye(3,5)
print(arr)
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]]

# 4. diag([values]) it creates a two dimen. array with all the diagonal elements as the given value and rest as 0 (in square matrix)
arr = np.diag([1,2,3,4])
print(arr)
diagonal_elements = np.diag(arr)
print(diagonal_elements)
# [[1 0 0 0]
#  [0 2 0 0]
#  [0 0 3 0]
#  [0 0 0 4]]
# [1 2 3 4]

# 5. randint---> this function is used to generate a random number betweem a given range.
# rand(min,max,total_values)
arr = np.random.randint(1,11,3)
arr2 = np.random.randint(20,41,5)
print(arr)
print(arr2)
floatarr = np.random.rand(5)#gives 5 different values between 0 and 1   
print(floatarr)
matrix2d = np.random.rand(3,5)# return 2D matrix filled with random number between 0 nd 1 
print(matrix2d)
# [6 6 3]
# [34 33 25 34 36]
# [0.83552013 0.19714826 0.9575114  0.57211433 0.80817689]
# [[0.80330681 0.61059009 0.5455088  0.24601691 0.86520354]
#  [0.55047036 0.13216529 0.14968204 0.08551771 0.92754207]
#  [0.49982131 0.27109817 0.49657847 0.27502004 0.5252126 ]]

# 6. randn ---> it is used to generate a random values centred to 0). this may return positive as well as negative number
arr = np.random.randn(5)
print(arr)
# [-0.42598881  2.44647462  1.51511125 -0.34096532  0.80438202]