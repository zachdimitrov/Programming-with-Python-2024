def decimal_to_n(base: int, number: int):
    converted = ""
    while number > 0:
        converted += str(number % base)
        number = number // base
    return converted[::-1]


line = input().split()
base = int(line[0])
num = int(line[1])

print(decimal_to_n(base, num))

