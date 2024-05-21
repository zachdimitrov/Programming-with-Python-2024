num = int(input())

for i in range(1, num + 1):
    order = str(i)
    digits_sum = 0
    for char in order:
        digits_sum += int(char)
    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')
