# for i in range(10):
#     print("i is now {} ".format(i))

#   basic difference btw for and while loops

# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1

available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break
else:
    print("Aren't you gald , you got out!")