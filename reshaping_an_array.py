# reshaping of an array -----> 1D to 2D/3D and vice versa
import numpy as np
arr = np.random.randint(1,51,12)
rows,column=3,4
arr=arr.reshape(rows,column)
print(arr)
# [[39 35  4 47]
#  [26  7  7 33]
#  [ 7 10 48 43]]
arr2=arr.reshape(2,6)
arr3=arr.reshape(1,4,3)# convertind 2D to 3D
print(arr2)
# [[39 35  4 47 26  7]
#  [ 7 33  7 10 48 43]]

print(arr3)
# [[[39 35  4]
#   [47 26  7]
#   [ 7 33  7]
#   [10 48 43]]]

arr=arr2.reshape(12)# converting 2D to 1D
print(arr)

# [39 35  4 47 26  7  7 33  7 10 48 43]