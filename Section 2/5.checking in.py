#    in

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot.casefold():
    print("{} is in {}".format(letter,parrot))
else:
    print("I don't need that letter")

#    not in

activity = input("What would you like to do today? ")
if "cinema" not in activity.casefold():
    print("But i wanna go to the cinema")