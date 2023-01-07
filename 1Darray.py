# creating Numpy array ( one dimentional )
# since we have list in python then why we convert them into array and use it as array ? so, the answer is pretty simple ... array is more efficient and faster than list that's the reason we use array
import numpy as np
a=list(range(1,11))
array =np.array(a)
print(array)
# array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
numbers=[int(i) for i in input("enter the values you want to insert in an array:\t").split(' ')]
array = np.array(numbers)
print(array)
# enter the values you want to insert in an array:	1 2 3 4 1 5 1 2 6 1 4 5 8 9 4 1 2 3 5 7 8 56 4
# array([ 1,  2,  3,  4,  1,  5,  1,  2,  6,  1,  4,  5,  8,  9,  4,  1,  2,
#         3,  5,  7,  8, 56,  4])