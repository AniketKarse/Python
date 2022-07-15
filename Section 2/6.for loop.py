#       Range

for i in range(0, 10 ,2):     #try this (10, 0, -2)
    print("i is now {} ".format(i))
print()

#       Nested for loop

for i in range(1, 13):
    for j in range(1, 13):
        print("{0} times {1} is {2} ".format(j, i, i*j))
    print("-------------------------------------------")