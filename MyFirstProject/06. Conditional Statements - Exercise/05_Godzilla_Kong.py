budget = float(input())
statists = int(input())
clothes_price = float(input())

decor_price = budget * 0.1
if statists > 150:
    clothes_price -= clothes_price * 0.1

final_sum = decor_price + statists * clothes_price

if final_sum > budget:
    print('Not enough money!')
    print(f'Wingard needs {final_sum - budget:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {budget - final_sum:.2f} leva left.')
