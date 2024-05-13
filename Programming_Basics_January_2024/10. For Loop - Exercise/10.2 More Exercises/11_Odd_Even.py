from math import inf

n = int(input())

odd_sum = 0
odd_min = inf
odd_max = -inf
even_sum = 0
even_min = inf
even_max = -inf

for i in range(1, n + 1):
    number = float(input())

    if i % 2 == 0:
        even_sum += number
        if even_max < number:
            even_max = number
            no_even_min_max = False
        if even_min > number:
            even_min = number
            no_even_min_max = False
    else:
        odd_sum += number
        if odd_max < number:
            odd_max = number
            no_odd_min_max = False
        if odd_min > number:
            odd_min = number
            no_odd_min_max = False
    print('----------')
    print(f'Pos: {i} - Number: {number}')
    print(f'min: {odd_min} - {even_min}')
    print(f'max: {odd_max} - {even_max}')
    print('----------')

print(f'OddSum={odd_sum:.2f},')
if odd_min == inf:
    print(f'OddMin=No,')
else:
    print(f'OddMin={odd_min:.2f},')

if odd_max == -inf:
    print(f'OddMax=No,')
else:
    print(f'OddMax={odd_max:.2f},')

print(f'EvenSum={even_sum:.2f},')
if even_min == inf:
    print(f'EvenMin=No,')
else:
    print(f'EvenMin={even_min:.2f},')

if even_max == -inf:
    print(f'EvenMax=No')
else:
    print(f'EvenMax={even_max:.2f}')
