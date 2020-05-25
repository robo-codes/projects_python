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


'''day 11 2d arrays'''

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    arr = []
    a = []
    for _ in range(6):
        arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        a.append(arr)
    suml=[]
    def calculate(i,j):
        return(a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1] + a[i+2][j] + a[i+2][j+1] + a[i+2][j+2])
    for i in range(0,4):
        for j in range(0,4):
            sum=calculate(i,j)
            suml.append(sum)
    print(max(suml))


'''day 12 inheritance'''

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        a = sum(self.scores)/len(self.scores)
        if a<40:
            return("T")
        elif 40<=a<55:
            return("D")
        elif 55<=a<70:
            return("P")
        elif 70<=a<80:
            return("A")
        elif 80<=a<90:
            return("E")
        else:
            return("O")
line = input().split()


'''day 13 abstract class'''

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self,title,author,price):
        super().__init__(title,author)
        self.price=price
    def display(self):
        print("Title: "+title)
        print("Author: "+author)
        print("Price: "+str(price))

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()

'''day 14 scope'''

class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = max(self.__elements) - min(self.__elements)



# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)


'''day 15 linked list'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        new_node = Node(data)
        current = head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            head = new_node
        return head
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);


'''day 16 exception handling'''

#!/bin/python3

import sys


S = input().strip()
try:
    S=int(S)
    print(S)
except:
    print("Bad String")


'''day 17 more exception'''

#Write your code here
class Calculator(object):
    def power(self,n,p):
        if (n < 0) or (p < 0):
            raise Exception('n and p should be non-negative')
        else:
            return pow(n,p)

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)


''' day 18 queue and stack '''

import sys

class Solution(object):
    def __init__(self):
        self.__stack = []
        self.__queue = []
    def pushCharacter(self, s):
        self.__stack.append(s)
    def enqueueCharacter(self, s):
        self.__queue.insert(0,s)
    def popCharacter(self):
        return self.__stack.pop()
    def dequeueCharacter(self):
        return self.__queue.pop()
# read the string s
s=input()
#Create the Solution class object
obj=Solution()

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")


''' day 19 interfaces '''

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        s = 0
        for i in range(1,n+1):
            if n % i == 0:
                s += i
        return s

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)


'''day 20 sorting(bubble sort)'''

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numSwap = 0
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numSwap+=1
    if numSwap==0:
        break
firstElement = a[0]
lastElement = a[n-1]
print("Array is sorted in",numSwap,"swaps.")
print("First Element:",firstElement)
print("Last Element:",lastElement)

'''day 21 generics'''

'''#include <iostream>
#include <vector>
#include <string>

using namespace std;

/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

// Write your code here
template<typename T>
void printArray(vector<T> array) {
     for(T i : array){
          cout << i << endl;
     }
}

int main() {
	int n;

	cin >> n;
	vector<int> int_vector(n);
	for (int i = 0; i < n; i++) {
		int value;
		cin >> value;
		int_vector[i] = value;
	}

	cin >> n;
	vector<string> string_vector(n);
	for (int i = 0; i < n; i++) {
		string value;
		cin >> value;
		string_vector[i] = value;
	}

	printArray<int>(int_vector);
	printArray<string>(string_vector);

	return 0;
}'''

'''day 22 binary search tree'''

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if root:
            left = 0
            right = 0
        if root.left:
            left = 1 + self.getHeight(root.left)
        if root.right:
            right = 1 + self.getHeight(root.right)
        return max(left, right)
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)


'''day 23 binary search tree level traversal'''

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        if root:
            queue = [root]
            while queue:
                node = queue.pop()
                print(node.data, end=" ")
                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)


'''day 24 more linkedlist'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        previous = head
        s = set()
        s.add(previous.data)
        current = previous.next
        while current:
            if current.data in s:
                previous.next = current.next
            else:
                s.add(current.data)
                previous = current
            current = current.next
        return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head);

'''day 25 running time and complexity'''

def is_prime(n):
    if n == 1:
        return False
    else:
        sqrt = int(n**0.5)
        for i in range(2, sqrt + 1):
            if ((n % i) == 0) and (i != n):
                return False
        return True

T = int(input())
for _ in range(T):
    n = int(input())
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")
