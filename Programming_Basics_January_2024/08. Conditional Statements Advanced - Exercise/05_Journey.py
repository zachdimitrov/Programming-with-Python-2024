budget = float(input())
season = input()
spent = 0
place = ''
vacation_type = ''

if budget <= 100:
    if season == 'summer':
        spent = budget * 0.3
        place = 'Bulgaria'
        vacation_type = 'Camp'
    elif season == 'winter':
        spent = budget * 0.7
        place = 'Bulgaria'
        vacation_type = 'Hotel'
    else:
        print('error')
elif 100 < budget <= 1000:
    if season == 'summer':
        spent = budget * 0.4
        place = 'Balkans'
        vacation_type = 'Camp'
    elif season == 'winter':
        spent = budget * 0.8
        place = 'Balkans'
        vacation_type = 'Hotel'
    else:
        print('error')
elif budget > 1000:
    spent = budget * 0.9
    place = 'Europe'
    vacation_type = 'Hotel'

print(f'Somewhere in {place}')
print(f'{vacation_type} - {spent:.2f}')
