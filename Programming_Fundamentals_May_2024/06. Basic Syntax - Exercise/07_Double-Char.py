while True:
    command = input()
    if command == "End":
        break
    if command == 'SoftUni':
        continue
    stringToPrint = ''
    for letter in command:
        stringToPrint = stringToPrint + letter + letter
    print(stringToPrint)
