import math

execute = int(input('Select a function: \n'
                    '1 - is prime \n'
                    '2 - factorial \n'))


# is prime
def is_prime():
    num = int(input('Input a number: '))
    is_prm = True
    for i in range(2, num):
        if num % i == 0:
            is_prm = False
            break
    if is_prm:
        print(f'{num} is a prime number!')
    else:
        print(f'{num} is NOT a prime!')


def factorial():
    num = int(input('Input a number: '))
    print(f'Factorial of {num} is: {math.factorial(num)}')


if execute == 1:
    is_prime()
elif execute == 2:
    factorial()
