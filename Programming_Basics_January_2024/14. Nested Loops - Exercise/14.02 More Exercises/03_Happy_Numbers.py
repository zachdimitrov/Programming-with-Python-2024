n = int(input())

for i in range(1000, 10000):
    is_happy = True
    d_one = i // 1000 % 10
    d_two = i // 100 % 10
    d_three = i // 10 % 10
    d_four = i % 10

    if d_one == 0 or d_two == 0 or d_three == 0 or d_four == 0:
        is_happy = False

    if d_one + d_two != d_three + d_four or n % (d_one + d_two) != 0:
        is_happy = False

    if is_happy:
        print(str(i) + ' ', end='')

