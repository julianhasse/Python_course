letters = ["a", "b", "c", "d"]

for letter in letters:
    print(letter)

# this will return a tupple with the index and the item
for letter in enumerate(letters):
    print(letter)


# here we unpack the list in 2 variables
for index, letter in enumerate(letters):
    print(index, letter)
