budget = float(input())
season = input()
price = 0
place = ''
location = ''

if budget <= 1000:
    place = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.45

elif 1000 < budget <= 3000:
    place = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.80
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.60

elif budget >= 3000:
    place = 'Hotel'
    price = budget * 0.9
    if season == 'Summer':
        location = 'Alaska'
    elif season == 'Winter':
        location = 'Morocco'

print(f'{location} - {place} - {price:.2f}')
