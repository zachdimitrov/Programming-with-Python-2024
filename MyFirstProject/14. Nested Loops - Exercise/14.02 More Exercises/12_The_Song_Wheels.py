m = int(input())
counter = 0
password = 0
printed = False

for i in range(1000, 10000):
    is_ok = True
    d_one = i // 1000 % 10
    d_two = i // 100 % 10
    d_three = i // 10 % 10
    d_four = i % 10

    if d_one == 0 or d_two == 0 or d_three == 0 or d_four == 0:
        is_ok = False
    if d_one < d_two and d_three > d_four:
        pass
    else:
        is_ok = False
    if d_one * d_two + d_three * d_four != m:
        is_ok = False
    if is_ok:
        counter += 1
        if counter == 4:
            password = i
        print(str(i) + ' ', end='')
        printed = True

if printed:
    print()
if password != 0:
    print(f'Password: {password}')
else:
    print('No!')
