quantity = int(input())
days = int(input())
days_count = 0
budget = 0
spirit = 0

price_ornamental = 2
price_skirt = 5
price_garland = 3
price_lights = 15

points_ornamental = 5
points_skirt = 3
points_garland = 10
points_lights = 17

while days > 0:
    days_count += 1
    days -= 1
    if days_count % 11 == 0:
        quantity += 2
    if days_count % 2 == 0:
        budget = budget + quantity * price_ornamental
        spirit = spirit + points_ornamental
    if days_count % 3 == 0:
        budget = budget + quantity * (price_skirt + price_garland)
        spirit = spirit + points_skirt + points_garland
    if days_count % 5 == 0:
        budget = budget + quantity * price_lights
        spirit = spirit + points_lights
    if days_count % 15 == 0:
        spirit += 30
    if days_count % 10 == 0:
        spirit -= 20
        budget = budget + price_garland + price_skirt + price_lights

if days_count % 10 == 0:
    spirit -= 30

print(f'Total cost: {budget}')
print(f'Total spirit: {spirit}')
