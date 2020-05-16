''' #guess the number# user input , computer guesses one number , give user chances to guess the number , if can not give true output in chances given print the number! '''
import random
rndm = random.randint(0, 10)
n = 3
print("\nso we are playing the guessing number game ! you have to guess a number bitween 0-10")
while(n != 0):
    print("please guess the number bitween 1-10")
    try:
        user = int(input())
        if user == rndm:
            print("you did it !")
            break
        else:
            if user < rndm:
                print("\nyou should select a value greater than",user)
            else:
                print("\nyou should select a value less than",user)
    except:
        print("\nplease write an integer value between 1-10")
    n -= 1
if n == 0:
    print("you've exhousted the limit of guesses! thanks for playing and the answer was : ",rndm)
