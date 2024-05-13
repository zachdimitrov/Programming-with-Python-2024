start_int = int(input())
end_int = int(input())

for i in range(start_int * 1000, (end_int + 1) * 1000):
    is_ok = True
    d_one = i // 1000 % 10
    d_two = i // 100 % 10
    d_three = i // 10 % 10
    d_four = i % 10

    if start_int <= d_two <= end_int and \
            start_int <= d_three <= end_int and \
            start_int <= d_four <= end_int:
        pass
    else:
        is_ok = False
    if (d_one % 2 == 0 and d_four % 2 == 0) or (d_one % 2 != 0 and d_four % 2 != 0):
        is_ok = False
    if d_one <= d_four:
        is_ok = False
    if (d_two + d_three) % 2 != 0:
        is_ok = False
    if is_ok:
        print(str(i) + ' ', end='')
