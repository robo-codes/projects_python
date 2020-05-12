'''set'''

n,m = input().split()
l = input().split()
s1 = set(input().split())
s2 = set(input().split())
print(sum([(i in s1) - (i in s2) for i in l]))


'''set add'''

n = int(input())
s = set()
for i in range(n):
    a = str(input())
    s.add(a)
print(len(s))

'''set remove() pop() discard()'''

n = int(input())
s = set(map(int, input().split()))
c = int(input())
for i in range(c):
    a=[]
    a=input().split()
    if a[0]=="pop":
        s.pop()
    if a[0]=="remove":
        s.remove(int(a[1]))
    if a[0]=="discard":
        s.discard(int(a[1]))
print(sum(s))

'''set update() intersection() difference() symmetric_difference()'''

n = int(input())
set1 = set(input().split())
m = int(input())
set2 = set(input().split())
set3 = set1.union(set2)
set4 = set1.intersection(set2)
set5 = set1.difference(set2)
set6 = set1.symmetric_difference(set2)
print(len(set3),len(set4),len(set5),len(set6))

'''set mutation'''

a,set1 = int(input()),set(map(int,input().split()))
b = int(input())
for i in range(b):
    (command, newset)=((input().split())[0],set(map(int,input().split())))
    getattr(set1,command)(newset)
print(sum(set1))

'''plusminus'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    ps=0
    ng=0
    z=0
    for i in range(0,len(arr)):
        if arr[i]<0:
            ng+=1
        elif arr[i]==0:
            z+=1
        else:
            ps+=1
    ps = round((ps/len(arr)),6)
    ng = round(ng/len(arr),6)
    z = round(z/len(arr),6)
    print(ps)
    print(ng)
    print(z)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

'''staircase'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(1,n+1):
        print(str('#'*i).rjust(n))
if __name__ == '__main__':
    n = int(input())

    staircase(n)

'''min-max'''

!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr=sorted(arr)
    s=0
    s3=arr[1:]
    s1=arr[:len(arr)-1]
    s2=0
    s=sum(s3)
    s2=sum(s1)
    print(s2,s)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

'''birthday candle'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    count=0
    m=max(ar)
    for i in range(0,len(ar)):
        if ar[i]==m:
            count+=1
    return(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

'''timeconverse'''

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[-2:]=="AM" and s[:2]=="12":
        return "00"+s[2:-2]
    elif s[-2:]=="AM":
        return s[:-2]
    elif s[-2:]=="PM" and s[:2]=="12":
        return s[:-2]
    elif s[-2:]=="PM" and s[:2]!="12":
        return str(int(s[:2])+12)+s[2:8]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()


'''superReducedString'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    if not s:
        return "Empty String"
    for i in range(0,len(s)):
        if i<(len(s)-1):
            if s[i]==s[i+1]:
                return (superReducedString(s[:i]+s[i+2:]))
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()

'''camelcase'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    count=1
    for i in range(0,len(s)):
        if s[i].isupper():
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()

'''strong password'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    count=0
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    if any(i in numbers for i in password)==False:
        count+=1
    if any(i in lower_case for i in password)==False:
        count+=1
    if any(i in upper_case for i in password)==False:
        count+=1
    if any(i in special_characters for i in password)==False:
        count+=1
    return(max(count,6-n))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()


'''day 8 hackerrank'''

n=int(input())
pb=dict()
for i in range(n):
    x=input().split()
    pb[x[0]]=x[1]
while True:
    try:
        search=input()
        if search in pb.keys():
            output=''.join("%s=%r"%(search,int(pb[search])))
            print (output)
        else:
            print("Not found")
    except EOFError:
            break

'''factorial reccursion'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    fact=0
    if n<=1:
        return(1)
    for i in range(n,1,-1):
        fact=n*factorial(n-1)
    return(fact)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()

'''day 10 hackerrank'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    b=(bin(n)[2:])
    count=0
    max_count=0
    for i in b:
        if i=='1':
            count+=1
        else:
            if count>max_count:
                max_count=count
            count=0
    if count>max_count:
        max_count=count
    print(max_count)
