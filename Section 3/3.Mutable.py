list = ["computer", 
        "moniter",
        "keyboard",
        "mouse",
        "mousepad"
        ]

another_list = list
print(id(list))
print(id(another_list))

list += ["joystick"]
print(id(list))
print(id(another_list))

#       see both mutable and immutable objects to observe the difference

a = b = c = d = e = f = another_list
print(a)
print("Adding Light pen")
b.append("light pen")
print(c)
print(d)