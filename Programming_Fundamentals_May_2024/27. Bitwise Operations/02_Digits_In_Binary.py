number = int(input())
digit = int(input())
count = 0

while number != 0:
    left = number % 2
    if left == digit:
        count += 1
    number = number // 2
print(count)
