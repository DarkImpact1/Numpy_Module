import numpy as np
finallist=[]
for i in range(3):
    sublist=[]
    for j in range(2):
        sublist.append(int(input()))
    finallist.append(sublist)
array2d=np.array(finallist)
print(array2d)
# 1
# 2
# 3
# 4
# 5
# 6
# array([[1, 2],
#        [3, 4],
#    [5, 6]])
array2d=[[int(i) for i in input("enter numbers\t").split(",")] for i in range(int(input("number of rows:\t")))]
arr=np.array(array2d)
print("dimention of array = ", arr.ndim)
# number of rows:	3
# enter numbers	1,2,3
# enter numbers	4,5,6
# enter numbers	7,8,9
# dimention of array =  2
a=[[1,2,3],[4,5,6],[1,2,6],[5,6,8]]
arr=np.array(a)
print(arr)
print("dimention of array is ",arr.ndim,"D")
print("shape of dimention is : ", arr.shape)
row,column=arr.shape[0],arr.shape[1]
print("Rows",row,"Column",column)
# [[1 2 3]
#  [4 5 6]
#  [1 2 6]
#  [5 6 8]]
# dimention of array is  2 D
# shape of dimention is :  (4, 3)
# Rows 4 Column 3