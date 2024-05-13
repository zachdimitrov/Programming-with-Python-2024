fuel = input()
liters = float(input())
club_card = input()

price = 0

if fuel == 'Gas':
    price = liters * (0.93 - 0.08) if club_card == 'Yes' else liters * 0.93
elif fuel == 'Gasoline':
    price = liters * (2.22 - 0.18) if club_card == 'Yes' else liters * 2.22
elif fuel == 'Diesel':
    price = liters * (2.33 - 0.12) if club_card == 'Yes' else liters * 2.33

if 20 <= liters <= 25:
    price = price - price * 0.08
elif liters > 25:
    price = price - price * 0.1

print(f'{price:.2f} lv.')
