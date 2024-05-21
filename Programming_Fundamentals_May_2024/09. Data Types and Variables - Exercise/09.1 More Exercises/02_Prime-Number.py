to_check = int(input())
is_prime = True
for i in range(2, int(to_check / 2)):
    if to_check % i == 0:
        is_prime = False
if is_prime:
    print('True')
else:
    print('False')
