# no need to initialize "command"

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
