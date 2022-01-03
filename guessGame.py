import random as r

number = r.randrange(100)
Guess = 5

while Guess >= 0:
    your_guess = int(input("Enter Your Guess "))

    def check(x):
        if your_guess >= x:
            print('You win')
        elif your_guess > x:
            print("Your are too high")
        else:
            print("your are too lower")


    if Guess > 1:
        check(number)
    elif Guess == 1:
        check(number)
        print("This is your last Chance")
    else:
        print("You lost")

    Guess = Guess - 1
