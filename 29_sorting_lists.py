# numbers = [1, 5, 21, 123, 0, 2]
# numbers.sort()
# # or
# numbers.sort(reverse=True)
# print(numbers)

# print(sorted(numbers))
# print(numbers)

# Sorting using Lambda Functions

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]


# lambda function syntax: lambda parameter(s):expresion
items.sort(key=lambda item: item[1])
print(items)
