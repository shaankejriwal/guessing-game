import random

number = random.randint(1,10)
guess = 0

while guess != number:
    guess = input("input any guess of number between 1 to 10")
    guess = int(guess)

if guess <= 5 & guess == number:
    print("well done , u guessed the correct nuumber")
    break
else:
    print("please try again , u guessed the wrong number")