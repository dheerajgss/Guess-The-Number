import random

print("Hello and welcome to Guess The Number!\n")
print("The computer will choose a random number from 1 to 100.")
print("You have to guess the number until you get the computer's value.")
print("If your number is greater than computer's, then 'Too high' will be displayed.")
print("If your number is lesser than computer's, then 'Too low' will be displayed.\n")

game = True
t = random.randint(1,101)
while(game):
    print("Computer has chosen a number!")
    while(True):
        n = int(input("Enter your number: "))
        if(n == t):
            print("IT'S A MATCH!!!")
            break
        elif(n < t):
            print("Too low")
        else:
            print("Too high")
    ch = input("Do you want to play again?(y/n): ")
    if(ch == 'y' or ch == 'Y' or ch == 'yes' or ch == 'Yes'):
        game = True
        t = random.randint(1,101)
    elif(ch == 'n' or ch == 'N' or ch == 'No' or ch == 'no'):
        game = False
        print("Goodbye!")
    else:
        print("I think you are testing the program. So, I'm quitting!!!")
        game = False
