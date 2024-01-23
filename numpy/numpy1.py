import numpy as np

a = np.array([1,2,3], dtype='int32')
print(a)

b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

#Get Dimension
print(a.ndim)
print(b.ndim)

#Get shape
print(a.shape)
print(b.shape)

#Get type
print(a.dtype)
print(b.dtype)

#Get Size
print(a.itemsize)
print(b.itemsize)

#Get total size
print(a.size) #Num of elements 
print(a.size * a.itemsize) #Total size of all elements
print(a.nbytes) #Same operation



#Accessing/Changing specific elements, rows, columns, etc
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

#Get a specific Element [r, c]
print(a[1, -2])

#Get a specific row
print(a[0, :])

#Get a specific column
print(a[:, 2])

#Getting a little more fancy [startindex:endindex:stepsize]
print(a[0, 1:6:2])

a[1,5] = 20
print(a)

a[:,2] = [1,2]
print(a)

#3-D Example
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

#Get a specific element (work outside in)
print(b[:,1,:])

#Replace
b[:,1,:] = [[9,9],[8,8]]
print(b)

#Initializing Different types of Arrays
#All 0s Matrix
print(np.zeros((2,3,3,2)))

#All 1s Matrix
print(np.ones((4,2,2),dtype='int32'))

#Any other number
print(np.full((2,2),99))

#Any other number (Full_like)
print(np.full_like(a, 4))

#Random Decimal numbers
print(np.random.rand(4,2))

print(np.random.random_sample(a.shape))

#Random int values
print(np.random.randint(7, size=(3,3)))

#The identity matrix
print(np.identity(7))

#Repeating the array
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis=0)
print(r1)





#Problem 1
output = np.ones((5,5))
print(output)

z = np.zeros((3,3))
z[1,1] = 9
print(z)

output[1:4,1:4] = z
print(output)




#Mathematics
a = np.array([1,2,3,4])
print(a)

print(a + 2)
print(a - 2)
print(a * 2)
print(a / 2)

b = np.array([1,0,1,0])
print(a + b)

print(a**2)

print(np.sin(a))
print(np.cos(a))

#Linear Algebra
a = np.ones((2,3))
print(a)

b = np.full((3,2),2)
print(b)

print(np.matmul(a,b))

#Find the determinant 
c = np.identity(3)
print(np.linalg.det(c))

#Statistics
stats = np.array([[1,2,3],[4,5,6]])
print(stats)

print(np.min(stats))

print(np.max(stats,axis=1))

print(np.sum(stats,axis=0))

#Reorganizing arrays
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape((4,2))
print(after)

#vertically stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack([v1,v2,v2,v2,v2]))


#Horizontal stacking
h1= np.ones((2,4))
h2 = np.zeros((2,2))

print(np.hstack((h1,h2)))


#Miscellaneous
#Load Data from File

file_data = np.genfromtxt('draft_data.txt',delimiter=',')
file_data = file_data.astype('int32')
print(file_data)

#Boolean Masking and Advanced indexing

print(file_data > 50)
print(file_data[file_data > 50])
print(np.any(file_data > 50, axis=0))

print(~((file_data > 50) & (file_data < 100)))