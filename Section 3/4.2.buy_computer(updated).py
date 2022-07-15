available_parts = ["computer",
                   "moniter",
                   "keyboard",
                   "mouse",
                   "hdmi cable",
                   "dvd"
                   ]

#valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]               //advanced code

valid_choices = []
for i in range (1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices) 
current_choice = "-"
computer_parts = []     # create an empty list

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # its already in the list, so remove it
            print("Removing {}". format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}". format(current_choice))
            computer_parts.append(chosen_part)
        print("Your lsit now contains {}".format(computer_parts))
        
    else:
        print("Please add the options from the list below: ")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

        # for part in available_parts:           # another way of looping
        #     print("{0}: {1}".format(available_parts.index(part) + 1, part))

    current_choice = input()

print(computer_parts)