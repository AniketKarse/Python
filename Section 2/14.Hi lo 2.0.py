low = 1
high = 1000
print("Please think of a number between {} and {} ".format(low, high))
input("Please press ENTER to start: ")

guesses = 1
while high != low:                                                #   NEW in 2.0
    # print("\tGuessing in the range of {} to {} ".format(low ,high))
    guess = low + (high - low) // 2
    high_low = input("my guess is {}. Should i guess higher or lower? Enter h or l , or c if my guess is correct ".format(guess)).casefold()

    if high_low == "h":
        # Guess higher. the low end of the range becomes 1 greater than the guess
        low = guess + 1
    elif high_low == "l":
        # Guess lower. the high end of the range becomes 1 less than the guess
        high = guess - 1
    elif high_low == "c":
        print("I got it right in {} guesses".format(guesses))
        break
    else:
        print("Please enter h, l or c ")
    #guesses = guesses + 1
    guesses += 1
else:                                                             #   NEW in 2.0
    print("You thought of a number {}".format(low))
    print("I got it in {} guesses".format(guesses))