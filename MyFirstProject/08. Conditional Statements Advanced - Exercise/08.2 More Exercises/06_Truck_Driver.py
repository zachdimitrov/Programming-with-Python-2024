season = input()
km_per_month = float(input())
wage = 0

if km_per_month <= 5000:
    if season == 'Spring' or season == 'Autumn':
        wage = km_per_month * 0.75
    elif season == 'Summer':
        wage = km_per_month * 0.9
    elif season == 'Winter':
        wage = km_per_month * 1.05
elif 5000 < km_per_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        wage = km_per_month * 0.95
    elif season == 'Summer':
        wage = km_per_month * 1.10
    elif season == 'Winter':
        wage = km_per_month * 1.25
elif 10000 < km_per_month <= 20000:
    wage = km_per_month * 1.45

wage *= 4
wage -= wage * 0.1
print(f'{wage:.2f}')
