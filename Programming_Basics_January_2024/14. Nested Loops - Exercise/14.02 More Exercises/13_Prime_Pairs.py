def is_prime(x):
    is_pr = True
    for p in range(2, x):
        if x % p == 0:
            is_pr = False
    return is_pr


first_two = int(input())
second_two = int(input())
first_diff = int(input())
second_diff = int(input())
first = 0
second = 0

for i in range(first_two, first_two + first_diff + 1):
    if is_prime(i):
        first = i
    else:
        continue
    for j in range(second_two, second_diff + second_two + 1):
        if is_prime(j):
            second = j
        else:
            continue
        print(str(i) + str(j))
