prime_sum = 0
non_prime_sum = 0
while True:
    text = input()
    if text == 'stop':
        break
    else:
        number = int(text)
        if number < 0:
            print('Number is negative.')
            continue
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
        if is_prime:
            prime_sum += number
        else:
            non_prime_sum += number
print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')
