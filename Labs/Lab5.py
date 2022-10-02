import random as r
num = r.randrange(1,100)
guess = 0

while not (guess == num):
    guess = int(input('Guess a number (1-100)'))
    if guess == num:
        print("you are winner")
        continue
    if guess < num:
        print("you are less")
    if guess > num:
        print("you are more")
        
