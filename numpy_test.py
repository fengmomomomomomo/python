import numpy as np

arr1 = np.array([[1,2,3],[2,3,4]])
print( arr1)
print( arr1.dtype)

arr2 = np.array([1.2,2.4,3.6])
print( arr2)
print( arr2.dtype)


print( arr2 +  arr1)

print(np.zeros((3,5)))

arr3 = np.arange(10)
print(arr3)
print(arr3[5])
print(arr3[5:8])
arr3[5:8] = 6
print(arr3)

arr4 = arr3.copy()


