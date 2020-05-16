'''Write a function to compute 5/0 and use try/except to catch the exceptions.'''

def compute():
    try:
        a = 5 / 0
    except Exception as e:
        return e
print(compute())

'''Implement a Python program to generate all sentences where subject is in ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].

Hint: Subject,Verb and Object should be declared in the program as shown below.

subjects=["Americans ","Indians"] verbs=["play","watch"] objects=["Baseball","Cricket"]

Output should come as below:

Americans  play Baseball. Americans  play Cricket. Americans  watch Baseball. Americans  watch Cricket. Indians play Baseball. Indians play Cricket. Indians watch Baseball. Indians watch Cricket.
'''

subjects=["Americans","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
for i in subjects:
    for j in verbs:
        for k in objects:
            print(i,j,k, end=".\n")


'''Write a function so that the columns of the output matrix are powers of the input vector.
The order of the powers is determined by the increasing boolean argument. Specifically, when increasing is False, the i-th output column is the input vector raised element-wise to the power of N - i - 1.

HINT: Such a matrix with a geometric progression in each row is named for Alexandre Theophile Vandermonde.
'''

def generate_vandermonde_matrix(l, p=5, isdescending=False):
    if isdescending:
        return [[i**j for j in range(p, -1, -1)] for i in l]
    return [[i**j for j in range(p+1)] for i in l]

print('Ascending:')
print(generate_vandermonde_matrix([1,2,3,4,5], 2))
print('Descending:')
print(generate_vandermonde_matrix([1,2,3,4,5], 4, isdescending=True))
