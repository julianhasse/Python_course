letters = ["a", "b", "c", "d"]

print(letters[0])

letters[0] = "Julian"

for item in range(len(letters)):
    print(letters[item])

# slicing a string
print(letters[0:3])  # returns 3 first items
print(letters[:3])  # zero is assumed
print(letters[0:])  # from first to the final item are returned
print(letters[:])  # a copy of the list is returned
print(letters[::2])  # returns every other element on the list
print(letters[::-1])  # returns every element on the list in reversed order

numbers = list(range(20))
print(numbers[::2])
print(numbers[::-1])
