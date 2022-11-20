import Constantes
import numpy as np
new_arr = np.array([1,2,3,4,5,6,7,8,])
print(new_arr)

arr = np.array((1,2,3,4,5))
print(arr)
#2-D array
arr1 = np.array([[1,23,4],[10,20,30]])
print(arr1)

#3D array
arr3 = np.array([[[1,2,3],[25,35,45],[80,90,100]]])
print(arr3[0,2,2])

a=np.array([1,2,3])
b= np.array([10,20,30])
c= a*b
print(c)