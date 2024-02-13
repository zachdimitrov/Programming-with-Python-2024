from math import inf

number = -inf
while True:
    command = input()
    if command == 'Stop':
        print(number)
        break

    new_number = int(command)
    if new_number > number:
        number = new_number
