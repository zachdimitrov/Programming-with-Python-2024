flower = input()
number = int(input())
budget = int(input())
price = 0

if flower == 'Roses':
    if number > 80:
        price = 5 - 5 * 0.1
    else:
        price = 5
elif flower == 'Dahlias':
    if number > 90:
        price = 3.8 - 3.8 * 0.15
    else:
        price = 3.8
elif flower == 'Tulips':
    if number > 80:
        price = 2.8 - 2.8 * 0.15
    else:
        price = 2.8
elif flower == 'Narcissus':
    if number < 120:
        price = 3 + 3 * 0.15
    else:
        price = 3
elif flower == 'Gladiolus':
    if number < 80:
        price = 2.5 + 2.5 * 0.2
    else:
        price = 2.5

check = price * number

if budget >= check:
    print(f'Hey, you have a great garden with {number} {flower} and {budget - check:.2f} leva left.')
else:
    print(f'Not enough money, you need {check - budget:.2f} leva more.')
