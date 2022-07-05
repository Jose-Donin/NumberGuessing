import random

#declare a variable for the pc to get the number
#create a variable for user input
#global variables, go before the function

number = random.randrange()
guess = int(input(""))

def numberGuessing():
    number = random.randrange(1, 10)
    guess = int(input("Enter a number: "))
    while number != guess:
        if guess < number:
            print("Try again fella, too low!")
            guess = int(input("Guess again: "))
        elif guess > number:
            print("Too high, like me and stuff")
            guess = int(input("Try again: "))
        else:
            break
    print("Uhul!")

numberGuessing()