budget = float(input())
category = input()
people = int(input())
price = 0

if 1 <= people <= 4:
    budget -= budget * 0.75
elif 5 <= people <= 9:
    budget -= budget * 0.6
elif 10 <= people <= 24:
    budget -= budget * 0.5
elif 25 <= people <= 49:
    budget -= budget * 0.4
elif people >= 50:
    budget -= budget * 0.25

if category == 'VIP':
    price = 499.99 * people
else:
    price = 249.99 * people

if budget >= price:
    print(f'Yes! You have {budget - price:.2f} leva left.')
else:
    print(f'Not enough money! You need {price - budget:.2f} leva.')
