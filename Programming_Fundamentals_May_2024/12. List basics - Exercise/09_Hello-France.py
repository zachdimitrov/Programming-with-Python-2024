items = input().split("|")
budget = float(input())
is_ok = True
bought = []
profit = 0
money = 0

for c in items:
    item = c.split("->")
    item_type = item[0]
    item_price = float(item[1])

    if item_type == "Clothes" and item_price > 50:
        is_ok = False
    elif item_type == "Shoes" and item_price > 35:
        is_ok = False
    elif item_type == "Accessories" and item_price > 20.5:
        is_ok = False

    if is_ok:
        if budget >= item_price:
            bought.append(item_price + item_price * 0.4)
            budget -= item_price
            money += item_price
            profit += item_price * 0.4
        else:
            continue
    is_ok = True

for elm in bought:
    print(f'{elm:.2f}', end=" ")

print("")
print(f"Profit: {profit:.2f}")
if budget + profit + money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
