months = int(input())

electricity = 0
water = 0
internet = 0
other = 0

for i in range(0, months):
    el_bill = float(input())
    electricity += el_bill
    water += 20
    internet += 15

    all_month = el_bill + 20 + 15
    other += all_month + all_month * 0.2

print(f'Electricity: {electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {(electricity + internet + water + other) / months:.2f} lv')

