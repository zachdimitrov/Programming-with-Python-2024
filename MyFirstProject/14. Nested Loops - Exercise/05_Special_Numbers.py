n = int(input())

for i in range(1111, 10000):
    number = str(i)
    is_special = True
    for ch in number:
        digit = int(ch)
        if digit == 0:
            is_special = False
            continue
        elif n % digit != 0:
            is_special = False
    if is_special:
        print(str(i) + ' ', end='')
