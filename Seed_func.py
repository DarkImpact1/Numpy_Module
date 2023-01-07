# we know that randint() generate random numbers. Everytime we run the program new set of random number is generated. But what if we want to fix the genration of this random number In this case we use seed function , this generate fix set of random numbers
import numpy as np
np.random.seed(2)# in order to fix generation of number we are writing these
arr = np.random.randint(1,100,10)
print(arr.size) # 10

