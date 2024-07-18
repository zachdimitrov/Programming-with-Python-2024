book = {}
number = 0
while True:
    command = input()
    if "-" not in command:
        number = int(command)
        break
    data = command.split("-")
    book[data[0]] = data[1]

for i in range(number):
    name = input()
    if name in book.keys():
        print(f"{name} -> {book[name]}")
    else:
        print(f"Contact {name} does not exist.")
