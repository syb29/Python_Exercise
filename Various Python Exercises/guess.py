import random
n = random.randint(1,10)
guess = 0
while guess != n:
    guess = int(input('Guess a number: '))
    if guess > n:
        print('The number must be smaller')
    elif guess < n:
        print('The number must be greater')
    else:
        print('You win')



