# Combine two lists in a tuple format

list1 = [1, 2, 3]
list2 = [10, 20, 30]

combined_lists = list(zip(list1, list2))
print(combined_lists)

# add a string

combined_lists = list(zip("abc", list1, list2))
print(combined_lists)
