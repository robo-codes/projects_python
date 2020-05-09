import numpy as np
'''(1) Write a program which will find all such numbers which are divisible by 7 but are not a multiple
of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
comma-separated sequence on a single line.'''

for n in range(2000,3001):
    if n%7==0 and n%5!=0:
        print(n,end=",")



'''(2) Write a Python program to accept the user's first and last name and then getting them printed in
the the reverse order with a space between first name and last name.'''

first_name = str(input())
last_name = str(input())
full_name = first_name+" "+last_name
print(full_name)



'''(3) Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r(cube 3)'''

r=6
pie=np.pi
v=((4/3)*pie*r*r*r)
print(v)




'''(4) Write a program which accepts a sequence of comma-separated numbers from console and
generate a list'''

num = input("input some comma separated numbers:- ")
list = num.split(",")
print(list)




'''(5) Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

for i in range(1,6):
    for j in range (1,i+1):
        if j<=5:
            print("* ",end="")
    print("")
for i in range(4,0,-1):
    for j in range(i):
        print("* ",end="")
    print("")




'''Write a Python program to reverse a word after accepting the input from the user.
Sample Output:
Input word: AcadGild
Output: dilGdacA'''

word=str(input())
rev="".join(reversed(word))
print(rev)




'''Write a Python Program to print the given string in the format specified in the sample output.
WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
its citizens
Sample Output:
WE, THE PEOPLE OF INDIA,
        having solemnly resolved to constitute India into a SOVEREIGN, !
               SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
                 and to secure to all its citizens
'''
print("WE, THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN, !\n\t       SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC\n\t\tAnd to secure to all its citizens")
