budget = float(input())
nights = int(input())
price_night = float(input())
expenses_percent = int(input())

if nights > 7:
    price_night = price_night - price_night * 0.05

spent = price_night * nights + budget * expenses_percent / 100
if budget >= spent:
    print(f'Ivanovi will be left with {budget - spent:.2f} leva after vacation.')
else:
    print(f'{spent - budget:.2f} leva needed.')

