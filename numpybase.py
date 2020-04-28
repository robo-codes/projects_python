import numpy as np
a=np.array([1,2,3])
list= [1,2,3]
b=list*2
c=a*2
print (c)
print (b)

#ar=n.array([[1,2],[1,2]])
#print(ar)
'''mt=np.matrix([[1,2],[1,2]])
print(mt)
ar=np.array(mt)
print(ar)
arr=np.random.random((1,2))
print(arr)
arrr=np.random.randn(1,3)
print (arrr)
#print (arr.mean())
#print (arr.var())
ar1=arr.dot(arrr)
print(ar1)'''
ar=np.array([[1,2,3],[2,3,1]])
arr=np.array([[2,3,4],[1,3,3],[3,2,1]])
#print(ar*arr)
ar1=arr.T
#print(ar.dot(ar1))
print(ar1)
ar2=np.linalg.inv(ar1)
print(ar2)
