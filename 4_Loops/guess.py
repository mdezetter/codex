guess = 0
tries = 0

while guess != 6 and tries<5:
    guess = int(input("Guess the number: "))
    tries = tries+1

    if guess == 6:
        print('You got it!')
    elif guess != 6 and tries <4:
        print('Try again!')
    elif tries == 4:
        print('Last guess!')
    elif tries == 5:
        print('You are out of guesses. Try again later')
    else:
        print('Error')
