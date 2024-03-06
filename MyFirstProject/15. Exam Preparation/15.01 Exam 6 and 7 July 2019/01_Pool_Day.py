from math import ceil

people = int(input())
entry_fee = float(input())
chair_price = float(input())
umbrella_price = float(input())

budget = entry_fee * people + ceil(0.75 * people) * chair_price + ceil(people / 2) * umbrella_price
print(f'{budget:.2f} lv.')


