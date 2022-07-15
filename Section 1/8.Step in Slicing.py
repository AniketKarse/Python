#         012345678901234
#         43210987654321 (Negative)
parrot = "Norwegian Blue"

print(parrot[2:12:2])
print(parrot[2:12:3])

number = "9,223;123:336,765:245;566"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values]) 