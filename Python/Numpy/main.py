import numpy as np

lst = [1,2,3,4,5]
arr = np.array(lst)
print(arr)
print(type(arr))
print(arr.shape)

lst1 = [1,2,3,4,5,6]
lst2 = [2,5,6,9,8,7]
lst3 = [3,8,4,9,8,0]

arr1 = np.array([lst1, lst2, lst3])
print(arr1)
print(arr1.shape)

print(arr[1])
print(arr[0:2])
print(arr[:-1])
print(arr[::-1])
print(arr[::-2])


print(arr1[1])
print(arr1[:,1])
print(arr1[1,:1:2])
print(arr1[1,:3:])


# EDA

print(arr < 2)
print(arr[arr < 2])

print(arr1.reshape(6,3))


# Mechanism to create element

print(np.arange(1,20,2))
print(np.arange(1,20,2).reshape(2,5))
print(np.arange(1,20,2).reshape(5,2))
print(np.arange(1,20,2).reshape(5,2,1))

print(arr*arr)
print(arr1*arr1)

print(np.ones((4,4)))
print(np.zeros((5,5)))


print(np.random.randint(10,80,6).reshape(3,2))

print(np.random.randn(5,5))
print(np.random.random_sample((5,5)))