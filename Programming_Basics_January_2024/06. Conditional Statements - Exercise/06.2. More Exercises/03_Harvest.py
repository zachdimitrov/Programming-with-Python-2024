from math import floor, ceil
area = int(input())
grapes_per_sqm = float(input())
liters_needed = int(input())
workers = int(input())

liters_produced = area * grapes_per_sqm * 0.4 / 2.5

if liters_produced >= liters_needed:
    liters_left = liters_produced - liters_needed
    liters_worker = liters_left / workers
    print(f'Good harvest this year! Total wine: {floor(liters_produced)} liters.')
    print(f'{ceil(liters_left)} liters left -> '
          f'{ceil(liters_worker)} liters per person.')
else:
    print(f'It will be a tough winter! '
          f'More {floor(liters_needed - liters_produced)} liters wine needed.')
