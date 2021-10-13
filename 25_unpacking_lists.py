numbers = [1, 2, 3]

first = numbers[0]
second = numbers[1]
third = numbers[2]

# cleaner way (unpack the list)

first, second, third = numbers

# or

first, second, *other = numbers
first, *other, last = numbers
