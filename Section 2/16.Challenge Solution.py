choice = "-"
while choice != "0":
    if choice in "123456":
        print("You chose {} ".format(choice))
    else:
        print("Please choose your option: ")
        print("1.    Python")
        print("2.    Java")
        print("3.    Go swimming")
        print("4.    Have dinner")
        print("5.    Go to bed")
        print("6.    Go to hell!")
        print("0.    Exit")
    
    choice = input()
            