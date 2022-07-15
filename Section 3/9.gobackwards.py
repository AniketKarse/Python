data = [104, 105, 4, 110, 120, 130, 133, 150, 45, 160, 170, 183, 333, 185, 187, 306, 188, 191]

min_valid = 100
max_valid = 200

# for index in range (len(data) - 1, -1, -1):
    # if data[index] < min_valid or data[index] > max_valid:
        # del data[index]
        # print(index, data)

top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        del data[top_index - index]
        print(top_index - index, value)

print(data)