n = int(input())
left_sum = 0
right_sum = 0

for i in range (0, n):
    number = int(input())
    left_sum += number

for i in range (0, n):
    number = int(input())
    right_sum += number

if left_sum > right_sum:
    print(f'No, diff = {left_sum - right_sum}')
elif right_sum > left_sum:
    print(f'No, diff = {right_sum - left_sum}')
else:
    print(f'Yes, sum = {left_sum}')
