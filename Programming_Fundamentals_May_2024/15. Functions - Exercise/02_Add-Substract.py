def sum_numbers(a, b):
    return a + b


def subtract(a, b):
    return a - b


first = int(input())
second = int(input())
third = int(input())

print(subtract(sum_numbers(first, second), third))
