from math import inf

n = int(input())
max_diff = -inf
prev_value = 0
is_diff = False

for i in range(0, n):
    num1 = int(input())
    num2 = int(input())
    value = num1 + num2
    if i > 0:
        if value != prev_value:
            is_diff = True
            diff = abs(value - prev_value)
            if max_diff < diff:
                max_diff = diff
    prev_value = value
    print('--------')
    print(is_diff)
    print(value - prev_value)
    print(max_diff)
    print('---------')

if is_diff:
    print(f'No, maxdiff={max_diff}')
else:
    print(f'Yes, value={prev_value}')
