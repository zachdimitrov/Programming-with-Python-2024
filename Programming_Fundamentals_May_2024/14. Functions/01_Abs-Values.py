strings = input().split(" ")
numbers = []

for n in strings:
    number = float(n)
    numbers.append(number)

abs_numbers = []
for n in numbers:
    abs_number = abs(n)
    abs_numbers.append(abs_number)

print(abs_numbers)
