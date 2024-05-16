budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price + flour_price * 0.25
loaf_price = flour_price + eggs_price + (milk_price * 0.25)

loaf_count = 0
colored_eggs = 0

while budget >= loaf_price:
    loaf_count += 1
    colored_eggs += 3
    budget -= loaf_price
    if loaf_count % 3 == 0:
        colored_eggs = colored_eggs - (loaf_count - 2)

print(f'You made {loaf_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
