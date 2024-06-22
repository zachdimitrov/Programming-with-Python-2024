n = int(input())
numbers = []
filtered = []

for i in range(n):
    new_number = int(input())
    numbers.append(new_number)

command = input()
if command == "even":
    for elem in numbers:
        if elem % 2 == 0 or elem == 0:
            filtered.append(elem)

if command == "odd":
    for elem in numbers:
        if elem %2 != 0:
            filtered.append(elem)

if command == "negative":
    for elem in numbers:
        if elem < 0:
            filtered.append(elem)

if command == "positive":
    for elem in numbers:
        if elem >= 0:
            filtered.append(elem)

print(filtered)
