import random

 #  asks for your name and tells rules
print("Hello, whats your name?")
your_name = str(input("Enter your name: "))
print("Hey,", your_name + " I'm thinking of a number between 1-20 can you guess it?, you get 5 tries")

 #  generates a number between 1-20 and asks user their guess, also amount of tries, user gets 5 tries to get number right
secret_number = (random.randrange(1, 20))
turns = 0
your_guess = int(input("Enter your guess"))

 #  loops if you got the wrong answer, and breaks if you got the correct one and congratulates you
while True:
    turns += 1
    if turns == 5:
        print("Sorry your rounds are up, you lost!")
        break
    elif your_guess == secret_number:
        print("Correct, you got the number after ", turns)
        break
    elif your_guess > secret_number:
        print("Too high!, guess again")
        your_guess = int(input())
    elif your_guess < secret_number:
        print("Too low!, try again")
        your_guess = int(input())
