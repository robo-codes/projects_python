import functools

'''Write a Python Program to implement your own myreduce() function which works exactly like
Python's built-in function reduce()'''

def myreduce(func, sequence):
    result = sequence[0]
    for item in sequence[1:]:
        result = func(result, item)

    return result

def sum(x,y):
    return x+y

print ("Sum on list [1,2,3] using myreduce function "   + str(myreduce(sum, [1,2,3])) )

'''Write a Python program to implement your own myfilter() function which works exactly
like Python's built-in function filter()'''

def myfilter(func, sequence):
    result = []
    for item in sequence:
        if func(item):
            result.append(item)

    return result

def ispositive(x):
    if x <= 0:
        return False
    else:
        return True

print("Filter only positive Integers on list [0,-2,3,-4,5] using custom filter function"  + str(myfilter(ispositive, [0,-2,3,-4,5])))

'''Implement List comprehensions to produce the following lists.
Write List comprehensions to produce the following Lists
['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]'''

first_list = [letters for letters in "ACADGILD"]
second_list = [letters*i for letters in "xyz" for i in range(1,5)]
third_list = [letters*i for i in range(1,5) for letters in "xyz"]
fourth_list = [[numbers+i] for numbers in [2,3,4] for i in range(0,3)]
fifth_list = [[numbers+i for numbers in [2,3,4,5]] for i in range(0,3)]
sixth_list = [(numbers,numbers) for numbers in [1,2,3] for numbers in [1,2,3]]
print(first_list)
print(second_list)
print(third_list)
print(fourth_list)
print(fifth_list)
print(sixth_list)

'''Implement a function longestWord() that takes a list of words and returns the longest one. '''

def longestWord(ls):
    #l = ['raj','rutu','ruturaj']
    longest = ''
    for i in range(0,len(ls)):
        if len(ls[i]) > len(longest):
            longest = ls[i]
    return(longest)
l = input().split(',')
print(longestWord(l))


'''Write a Python Program(with class concepts) to find the area of the triangle using the below formula.

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

Function to take the length of the sides of triangle from user should be defined in the parent class and function to calculate the area should be defined in subclass.

 '''

class shape:
    def getSides(self):
        self.a = int(input('Enter the length of 1st side: '))
        self.b = int(input('Enter the length of 2nd side: '))
        self.c = int(input('Enter the length of 3rd side: '))

class triangle(shape):
    def Area(self):
        self.getSides()
        s = (self.a + self.b + self.c) / 2
        self.area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
        print("the area of triangle is :",self.area)

t1 = triangle()
t1.Area()


'''Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n. '''

def filter_long_words():
    l1 = list(input().split(','))
    n = int(input())
    l2 = []
    for i in l1:
        if len(i) > n:
            l2.append(i)
    return(l2)
print(filter_long_words())

'''Write a Python program using function concept that maps  list of words into a list of integers representing the lengths of the corresponding words​.
 Hint: ​If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
 Here 2,3 and 4 are the lengths of the words in the list. '''

l1 = list(input().split(','))
l2 = []
for i in l1:
    l2.append(len(i))
print(l2)


'''Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise'''

def vowel_check():
    c = str(input())
    vowels = "aeiouAEIOU"
    if c in vowels:
        return True
    else:
        False
print(vowel_check())
