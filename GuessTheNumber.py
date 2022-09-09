import random
import time

guesses_used = 0
guess = 0
number = random.randint(1, 30)
print('I am thinking of a number between 1 and 30.')
while guesses_used < 5:
    guess = int(input('Guess the number within 5 guesses...'))
    guesses_used = guesses_used + 1
    if guess < number:
        print('Too low, try again.')
    if guess > number:
        print('Too high, try again.')
    if guess == number:
        print('Congratulations.')
        time.sleep(5)
        break

if guess == number:
    guesses_used = str(guesses_used)
    print('Well done! You guessed correctlly in ' + guesses_used + ' guesses.')

if guess != number:
    number = str(number)
    print('Sorry, out of guesses. The number I was thinking of is ' + number)