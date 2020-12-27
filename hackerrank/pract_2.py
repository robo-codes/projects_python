import numpy as np
import math

b = [int(item) for item in input("Enter the list items: ").split()]
b = np.sort(b)
bin0=[]
bin1=[]
bin2 = []
bin3 = []

print("Arranging data in width size of 3: ")
r = round((max(b)+min(b))/3)

for i in range(0,9,3):
    new = []
    k = int(i/3)
    for j in range(len(b)):
        if (b[j]) < (min(b) + (k+1)*r) and (b[j]) >= (min(b) + k*r):
            new.append(b[j])
    bin0.append(new)
print("Bin with equal width: \n", bin0)

for i in range(0, 9, 3):
    k = int(i/3)
    new=[]
    mean = (b[i] + b[i+1] + b[i+2])/3
    for j in range(3):
        new.append(mean)
    bin1.append(new)
print("Bin by Mean: \n", bin1)

for i in range(0, 9, 3):
    k = int(i/3)
    new = []
    for j in range(3):
        if (b[i+j]-b[i]) <= (b[i+2]-b[i+j]):
            new.append(b[i])
        else:
            new.append(b[i+2])
    bin2.append(new)
print("Bin by Boundaries: \n", bin2)

for i in range(0, 9, 3):
    k = int(i/3)
    new = []
    for j in range(3):
        new.append(b[i+1])
    bin3.append(new)
print("Bin by Median: \n", bin3)
