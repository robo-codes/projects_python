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

print(first_list)
