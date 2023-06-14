import numpy as np
print(np.__version__)
# row vector
array = np.array([1,2,3,])
print(array)
# column vector
array1= np.array([[1],[2],[3]])
print(array1) 
# matrix--2D
matrix= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)
print("\n\n")
#3D array
array3D= np.array([[(1,2,3),(4,5,6),(7,8,9)],[(1,2,3),(4,5,6),(7,8,9)]])
print(array3D)
print("\n\n")
# zeros
zeros= np.zeros((3,3),dtype="int")
print(zeros)

print("\n\n")
#ones
ones=np.ones((4,3), dtype="int")
print(ones)
print("\n\n")
#full
full = np.full((4,3),12)
print(full)
#eye--identity matrix
eye = np.eye(3,dtype="int")
print(eye)
print("\n\n")
#arange
arange=np.arange(0,10,2) # 0--starting pt, 10 ending pt(10 is not included), 2--step size
print(arange)
print("\n\n")
#linspace 
linspace=np.linspace(0,2,9) # we need 9 values in between 0 to 2 (including 0 and 2) 
print(linspace)
print("\n\n")
# random--rand it gives values inbetween 0-1
rand = np.random.rand(5,3)*255
print(rand)
print("\n\n")
# random --randint
randInt=np.random.randint(5,size=(5,3))
print(randInt)
print("\n\n\nuhhu\n")
#shape,size,dtype, astype
shapeArr=np.array([(1.2,0.2,3),(4,5.99,6)])
print(shapeArr.shape)
print(shapeArr.size)
print(shapeArr.dtype)
print(shapeArr.astype(int))
print("\n\n")
#array addition
array2=np.array([(1.2,0.2,3),(4,5.99,6)])
print(array2*shapeArr)
print("\t\t")
#min and max
print(array2.min())
print(array2.max().astype(int))