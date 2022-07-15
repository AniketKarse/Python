panagram = "The quick brown fox jumps over the lazy dog"

letters = sorted(panagram)
print(letters)

numbers = [1.2, 5.4, 7.1, 4.9, 9.4, 8.5 ]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)

missing_letters = sorted("The quick brown fox jumped over the lazy dog",key=str.casefold)
print(missing_letters)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
        ]

names.sort(key=str.casefold)
print(names)