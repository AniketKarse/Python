answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please Guess Higher!")
    guess = int(input())
    if guess == answer:
        print("You've got it!")
    else:
        print("Sorry, you've not guessed correctly")
elif guess > answer:
    print("Please Guess Lower")
    guess = int(input())
    if guess == answer:
        print("You've got it!")
    else:
        print("Sorry, you've not guessed correctly")
else:
    print("You've got it!")