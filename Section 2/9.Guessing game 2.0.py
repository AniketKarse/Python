import random

highest = 100
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
guess = 0

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

while guess != answer:
    if guess == 0:
        print("Game over!")
        break
    if guess < answer:
        print("Please Guess Higher!")
    elif guess > answer:
        print("Please Guess Lower!")
    guess = int(input())
    if guess == answer:
        print("You've got it!")
    
