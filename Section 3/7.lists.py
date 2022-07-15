empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_num = sorted(numbers)
print(sorted_num)
print(numbers)

digits = list("431256987")
print(digits)
print()

#more_num = list(numbers)
#more_num = numbers[:]
more_num = numbers.copy()
print(more_num)
print(numbers is more_num)
print(numbers == more_num)