budget = float(input())
season = input()
klas = ''
tip = ''
price = 0

if budget <= 100:
    klas = 'Economy class'
    if season == 'Summer':
        price = budget * 0.35
        tip = 'Cabrio'
    elif season == 'Winter':
        price = budget * 0.65
        tip = 'Jeep'
elif 100 < budget <= 500:
    klas = 'Compact class'
    if season == 'Summer':
        price = budget * 0.45
        tip = 'Cabrio'
    elif season == 'Winter':
        price = budget * 0.8
        tip = 'Jeep'
elif budget > 500:
    klas = 'Luxury class'
    price = budget * 0.9
    tip = 'Jeep'

print(f'{klas}')
print(f'{tip} - {price:.2f}')
