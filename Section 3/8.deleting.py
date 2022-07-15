data = [4, 5, 104, 105, 110, 120, 130, 133, 150, 160, 170, 183, 185, 187, 188, 191, 350, 260]

# all sorts of tests!

#data = [4, 5, 104, 105, 110, 120, 130, 133, 150, 160, 170, 183, 185, 187, 188, 191]
#data = [104, 105, 110, 120, 130, 133, 150, 160, 170, 183, 185, 187, 188, 191, 350, 260]
#data = [4, 5, 104, 105, 110, 120, 130, 133, 150, 160, 170, 183, 185, 187, 188, 191, 350, 260]
#data = [104, 105, 110, 120, 130, 133, 150, 160, 170, 183, 185, 187, 188, 191]
#data = [4000, 5645, 1504, 1045, 1120, 1520, 1630, 1383, 1250, 1670, 1790, 4183, 6185, 8187, 3188, 1591, 3250, 2660]
#data = []

#       part 1

#del data[0:2]
#print(data)
## del data[16:]    # it won't work cause now the position of every element      
## print(data)      # has been changed adn the list is reduced to 16 elements
#
#del data[14:]       # is the correct code
#print(data)


#       part 2 (This code won't work , find the mistake)
# min_valid = 100
# max_valid = 200

# for index, value in enumerate(data):
#     if(value < min_valid) or (value > max_valid):
#         del data[index]

# print(data)

#   part 3

min_valid = 100
max_valid = 200

# process the lower value in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)
del data[:stop]
print(data)

# process the high values
start = 0 
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        # we have the index of the last item to keep.
        # Set 'start' to the position of the first
        # item to delete which is 1 after 'index' 
        start = index + 1
        break

print(start)    # for debugging
del data[start:]
print(data)
