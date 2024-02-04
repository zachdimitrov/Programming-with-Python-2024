from math import inf

n = int(input())
num_sum = 0
max_num = -inf

for i in range(0, n):
    number = int(input())
    num_sum += number
    if max_num < number:
        max_num = number

num_sum -= max_num
if max_num == num_sum:
    print('Yes')
    print(f'Sum = {num_sum}')
else:
    print('No')
    print(f'Diff = {abs(max_num - num_sum)}')
