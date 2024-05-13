budget = float(input())
liters = float(input())
day = input()

spent = 100 + liters * 2.1
if day == 'Saturday':
    spent -= spent * 0.1
else:
    spent -= spent * 0.2
if budget >= spent:
    print(f'Safari time! Money left: {budget - spent:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {spent - budget:.2f} lv.')
