# when we slice a sub-array from an array, it may be done by the tw ways. First is by making view and he second is using a copy
# of it . But there is some difference between bboth of them. If you make a view of an array, any changes made to the sub array
# will be  replicated to the original array whereas if you make any copy, any changes ade of copied sub array will not reflect
# on the original array
import numpy as np
a=np.array(list(range(1,11)))
slicing = a[3:6]
slicing[:]=0
print(a) # array([ 1,  2,  3,  0,  0,  0,  7,  8,  9, 10])
# by default it is in view mode 
# and original will be updated

import numpy as np
a=np.array(list(range(1,11)))
slicing = a[3:6].copy()
print(slicing)# [4 5 6]
slicing[:] = 0
print(slicing)# [0 0 0]
print(a) # [ 1  2  3  4  5  6  7  8  9 10]
# it meand original array will not be updated since it is in view mode