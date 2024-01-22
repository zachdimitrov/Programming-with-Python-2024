budget = float(input())
video = int(input())
processor = int(input())
ram = int(input())

price_video = 250
price_processor = price_video * video * 0.35
price_ram = price_video * video * 0.1

full_price = price_ram * ram\
             + price_processor * processor\
             + price_video * video

if video > processor:
    full_price -= full_price * 0.15

if full_price <= budget:
    print(f'You have {budget - full_price:.2f} leva left!')
else:
    print(f'Not enough money! You need {full_price - budget:.2f} leva more!')
