money_needed = float(input())
money = float(input())
all_days = 0
spent_days = 0

while True:
    action = input()
    spent = float(input())
    all_days += 1
    if action == 'save':
        money += spent
        spent_days = 0
    if action == 'spend':
        money -= spent
        spent_days += 1
        if money <= 0:
            money = 0
    if money >= money_needed:
        print(f'You saved the money for {all_days} days.')
        break
    if spent_days >= 5:
        print('You can\'t save the money.')
        print(f'{all_days}')
        break
