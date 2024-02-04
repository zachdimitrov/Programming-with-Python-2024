from math import inf

n = int(input())
largest = -inf
smallest = inf

for i in range (0, n):
    number = int(input())
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print(f'Max number: {largest}')
print(f'Min number: {smallest}')
