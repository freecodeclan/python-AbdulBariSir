# Guess a number between 1 to 10
import random

rand_num_generator = random.randint(1,10)

guess_num = 0

while guess_num != rand_num_generator:
    guess_num = int(input("Enter the num: "))

    if guess_num < rand_num_generator:
        print('Number is smaller')
    elif guess_num > rand_num_generator:
        print('Number is grater')
    else:
        print('You guessed the right answer👍')
