#same as task 01_Unique_Pin
first_limit = int(input())
second_limit = int(input())
third_limit = int(input())

first_digit = 0
second_digit = 0
third_digit = 0

for i in range(1, first_limit + 1):
    if i % 2 == 0:
        first_digit = str(i)
    else:
        continue
    for j in range(1, second_limit + 1):
        if j == 2 or j == 3 or j == 5 or j == 7:
            second_digit = str(j)
        else:
            continue
        for k in range(1, third_limit + 1):
            if k % 2 == 0:
                third_digit = str(k)
                print(first_digit, second_digit, third_digit)
            else:
                continue

