n = int(input())
is_finished = False
current = 1

for row in range(1, n + 1):
    for col in range(1, row + 1):
        if current > n:
            is_finished = True
            break
        print(str(current) + ' ', end='')
        current += 1
    if is_finished:
        break
    print()


