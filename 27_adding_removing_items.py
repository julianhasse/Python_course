letters = ["a", "b", "c"]

# Add item at the end
letters.append("Z")
print(letters)

# Add item at specific position]
letters.insert(2, "x")
print(letters)

# Remove item at the end
letters.pop()
print(letters)

# Remove item by content instead of index
letters.remove("c")
print(letters)

# Remove range of items
del letters[0:3]
print(letters)

# Remove all items on the list
letters = ["a", "b", "c"]
letters.clear()
print(letters)
