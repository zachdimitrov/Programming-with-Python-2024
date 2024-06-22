n = int(input())
sum_divisors = 0
for i in range(1, n - 1):
    if n % i == 0:
        sum_divisors += i

if sum_divisors == n:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
