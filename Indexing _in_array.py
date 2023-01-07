# same concept is used for indexing in array as we had learned in the case of list
import numpy as np
a=[0,1,2,3,4,5,6,7,8,9]
arr=np.array(a)
for i in range(arr.size):#remember syntax---
    print(arr[i],end=" ")
print()
add = 0
for i in range(arr.size):
    add+=arr[i]
print("sum of all elements is : \t",add)

print(arr[0:4])
print(arr[1:6:3])
# 0 1 2 3 4 5 6 7 8 9 
# sum of all elements is : 	 45
# [0 1 2 3]
# [1 4]