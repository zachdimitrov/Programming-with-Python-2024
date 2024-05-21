lost_fights = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

spent = 0
for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        spent += helmet_price
    if i % 3 == 0:
        spent += sword_price
    if i % 6 == 0:
        spent += shield_price
    if i % 12 == 0:
        spent += armor_price

print(f'Gladiator expenses: {spent:.2f} aureus')
