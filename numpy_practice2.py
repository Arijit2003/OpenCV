import numpy as np

arr=np.array([(1,2,3,4,45),(5,6,7,8,9)])
print(arr[0:,:2])
#reverse
print(arr[::-1])
# reshape
print(arr.reshape(1,10)) # no of elements should match
arr1D= np.array([1,2,3,4,45,5,6,7,8,9])
print("\n")
print(arr1D.reshape(5,2))
print("\n")
#append
arr2=np.array([1,2,3,4,5,6,7,8,9,10])
array = np.append(arr2,[80,40,56,79])  
print(array)
print(arr2)
# delete
print(np.delete(arr2,2))

#ravel --flatening operation
arrayx=np.array([(1,2,3,4),(5,6,7,8)])
arrayY=np.array([1,25,56])
arrayR=arrayx.ravel()
print(arrayx)
print("\n")
print(arrayR)
#concatenate
f_array=np.concatenate((arrayY,arrayR))
print(f_array)
print("\n")
#transpose
narray = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np.transpose(narray))
#copy
actualArray=np.array([1,2,3,4])
copiedArray=np.copy(actualArray)
print(copiedArray) 