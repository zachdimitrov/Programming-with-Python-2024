num_one = int(input())
num_two = int(input())
print(f'Before:\na = {num_one}\nb = {num_two}')
c = num_one
num_one = num_two
num_two = c
print(f'After:\na = {num_one}\nb = {num_two}')
