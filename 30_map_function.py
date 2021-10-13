# mapping data from a list into a single list
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = []
for item in items:
    prices.append(item[1])

print(prices)

# a more elegant way to achieve the same result

x = map(lambda item: item[1], items)
for item in x:
    print(item)
# or

prices = list(map(lambda item: item[1], items))
print(prices)
