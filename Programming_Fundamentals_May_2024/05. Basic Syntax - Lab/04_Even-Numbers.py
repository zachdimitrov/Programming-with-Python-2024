n = int(input())
all_even = True
for i in range(0, n):
    num = int(input())
    if num % 2 != 0:
        all_even = False
        print(f'{num} is odd!')
        break
if all_even:
    print('All numbers are even.')
