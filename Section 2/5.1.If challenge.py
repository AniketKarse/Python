name = input("What's your name? ")
age = int(input("Hello {}, how old are you? ".format(name)))
if 18 < age < 31:
    print("Welcome to Goa!")
else:
    if age <= 18:
        print("Please come back in {} years ".format(19 - age))
    else:
        print("You are too mature for this kind of fun!")