computer_parts = ["computer",
                   "moniter",
                   "keyboard",
                   "mouse",
                   "hdmi cable",
                   "dvd"
                   ]
print(computer_parts)

computer_parts[3] = "trackball"
print(computer_parts[3:])

computer_parts[3:] = "trackball"        #   the difference is important
print(computer_parts)

computer_parts[3:] = ["trackball"]      # in between these lines of code
print(computer_parts)