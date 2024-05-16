n = int(input())
for i in range(0, n):
    stringToCheck = input()
    pure = True
    for letter in stringToCheck:
        if letter == ',' or letter == '.' or letter == '_':
            pure = False
    if pure:
        print(f'{stringToCheck} is pure.')
    else:
        print(f'{stringToCheck} is not pure!')
