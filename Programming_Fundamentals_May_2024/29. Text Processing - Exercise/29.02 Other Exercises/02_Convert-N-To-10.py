def n_to_decimal(base: int, number: int):
    decimal = 0
    rev_number = str(number)[::-1]
    for i in range(len(rev_number)):
        digit = int(rev_number[i])
        decimal = decimal + (digit * (base ** i))
    return decimal


line = input().split()
base = int(line[0])
num = int(line[1])

print(n_to_decimal(base, num))
