print("Please choose your options from the list below: ")



print("""
1. Python
2. Java
3. Go swimming
4. Have dinner
5. Go to bed
6. Go to hell!
0. Exit
                """)
            
menu = int(input())

num = [1, 2, 3, 4, 5, 6, 0]

while menu not in num:
    print("You have print an invalid number")
    print("""
    1. Python
    2. Java
    3. Go swimming
    4. Have dinner
    5. Go to bed
    6. Go to hell!
    0. Exit
                    """)
                    
    menu = int(input())
    break
else:
    if menu == 1:
        print("Yeah , what a great decision! Python it is then.")
        
    elif menu == 2:
        print("Yeah , what a great decision! Java it is then.")
        
    elif menu == 3:
        print("Yeah , what a great decision! Swimming it is then.")
        
    elif menu == 4:
        print("Yeah , what a great decision! I'm really hungry.")
        
    elif menu == 5:
        print("Yeah , what a great decision! Sleep works just fine.")
        
    elif menu == 6:
        print("Yeah , not a great decision. Too early, don't you think?.")
        
    elif menu == 0:
        print("Exit it is then!")

    