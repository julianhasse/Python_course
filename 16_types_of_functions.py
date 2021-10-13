# 1- Functions that perform a tasks

def greet(name):
    print(f'{name}')


greet('Julian')


# 2- Functions that return a value (more reusable in different scenarios)
def get_greeting(name):
    return f'Hi {name}'


message = get_greeting('Julian!')
print(message)

file = open("content.txt", "w")
file.write(message)
